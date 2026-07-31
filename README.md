# firewall-Server

Firewall en Flask y otras herramientas de servidor.

---

## Cloud Server - Firewall en Flask

##  Descripción

Este proyecto es un servidor web con firewall de aplicación y rate limiting. Fue desarrollado en Termux (Android) y es parte de mi portafolio como estudiante de Ingeniería en Sistemas.

##  Características

- **Firewall de IP:** Bloquea o permite acceso según la IP del cliente.
- **Rate Limiting:** Limita el número de peticiones por IP (10 peticiones por minuto).
- **Logs:** Guarda todos los intentos de acceso y bloqueos.
- **Inicio automático:** El servidor arranca solo al ejecutar `./start_server.sh`.

##  Estructura del Proyecto
```
firewall-universitario/
├── app.py # Código principal del servidor
├── config.py # Configuración (IP permitida, límites)
├── start_server.sh # Script para iniciar el servidor
├── README.md # Esta documentación
└── .gitignore # Archivos que Git ignora
```

##  Instalación y Configuración

### Requisitos

- Termux (Android)
- Python 3.14+
- Flask

### Paso 1: Clonar el repositorio

git clone https://github.com/tuusuario/firewall-in-flask-and-others-server-tools.git
cd firewall-in-flask-and-others-server-tools

Paso 2: Configurar la IP permitida

echo 'export IP_PERMITIDA="192.168.1.XX"' >> ~/.bashrc
source ~/.bashrc

(Reemplaza 192.168.1.XX con la IP de tu dispositivo autorizado.)

Paso 3: Ejecutar el servidor

chmod +x start_server.sh
./start_server.sh

Paso 4: Probar

Desde otro dispositivo en la misma red:

curl http://[IP_DEL_ANDROID]:5000

## Logs

    flask.log: Logs del servidor (errores y actividad).

    accesos.log: Registro de accesos permitidos y denegados.

    rate_limit.log: Registro de IPs bloqueadas por rate limiting.

## Tecnologías Utilizadas

    Python 3.14

    Flask 3.1.8

    Termux (Android)

    Git y GitHub

 Autor

[Cloud] - Estudiante 

Este proyecto es de código abierto. Puedes usarlo, modificarlo y compartirlo libremente.