#!/bin/bash
# Iniciar servidor Flask en segundo plano
cd ~
nohup python app.py > flask.log 2>&1 &  # Redirige salida a flask.log
echo $! > flask.pid                     # Guarda el PID para detenerlo después
echo "Servidor Flask iniciado en http://127.0.0.1:5000"
echo "Logs guardados en flask.log"
