import os
#Variable del entorno
IP_PERMITIDA = os.environ.get("IP_PERMITIDA", "127.0.0.1")
#Peticiones al server permitdas
LIMITE_PETICIONES = 10
VENTANA_TIEMPO = 60
TIEMPO_BLOQUEO = 300
