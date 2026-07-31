from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from config import IP_PERMITIDA, LIMITE_PETICIONES, VENTANA_TIEMPO, TIEMPO_BLOQUEO

# Diccionario para guardar el historial de peticiones de cada IP
historial_peticiones = {}

# Diccionario para guardar el momento en que una IP fue bloqueada
ip_bloqueadas = {}

# ============================================
# FUNCIONES DE RATE LIMITING
# ============================================

def limpiar_historial(ip, ahora):
    """Elimina las peticiones más viejas que la ventana de tiempo."""
    if ip in historial_peticiones:
        timestamps = historial_peticiones[ip]
        tiempo_limite = ahora - timedelta(seconds=VENTANA_TIEMPO)
        historial_peticiones[ip] = [t for t in timestamps if t > tiempo_limite]

def verificar_rate_limit(ip):
    """Verifica si la IP ha excedido el límite de peticiones."""
    ahora = datetime.now()

    # 1. Verificar si la IP está bloqueada
    if ip in ip_bloqueadas:
        tiempo_bloqueado = ip_bloqueadas[ip]
        tiempo_transcurrido = (ahora - tiempo_bloqueado).total_seconds()

        if tiempo_transcurrido < TIEMPO_BLOQUEO:
            return False, "Demasiadas peticiones. Espera 5 minutos."
        else:
            del ip_bloqueadas[ip]

    # 2. Limpiar el historial de peticiones viejas
    limpiar_historial(ip, ahora)

    # 3. Agregar la petición actual al historial
    if ip not in historial_peticiones:
        historial_peticiones[ip] = []
    historial_peticiones[ip].append(ahora)

    # 4. Verificar si la IP ha excedido el límite
    if len(historial_peticiones[ip]) > LIMITE_PETICIONES:
        ip_bloqueadas[ip] = ahora
        return False, "Demasiadas peticiones. Has sido bloqueado por 5 minutos."

    return True, None

# ============================================
# APLICACIÓN FLASK
# ============================================

app = Flask(__name__)

@app.route("/get_ip_client", methods=["GET"])
def get_ip_client():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/")
def home():
    ip_cliente = request.remote_addr
    ahora = datetime.now()

    # 1. Verificar rate limiting
    permitido, mensaje = verificar_rate_limit(ip_cliente)
    if not permitido:
        with open("rate_limit.log", "a") as log:
            log.write(f"{ahora} - IP bloqueada: {ip_cliente} - {mensaje}\n")
        return jsonify({"mensaje": mensaje, "ip": ip_cliente}), 429

    # 2. Verificar IP permitida (firewall original)
    if ip_cliente == IP_PERMITIDA:
        with open("accesos.log", "a") as log:
            log.write(f"{ahora} - IP: {ip_cliente} - ACCESO PERMITIDO\n")
        return jsonify({"mensaje": "Acceso permitido", "ip": ip_cliente}), 200
    else:
        with open("accesos.log", "a") as log:
            log.write(f"{ahora} - IP: {ip_cliente} - ACCESO DENEGADO\n")
        return jsonify({"mensaje": "Acceso denegado", "ip": ip_cliente}), 403

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
