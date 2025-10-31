# 🏠 Proyecto de Casa Domótica con Python

## 📘 Descripción

Este proyecto implementa un sistema de **casa domótica inteligente** desarrollado en **Python**, orientado a la automatización, monitoreo y control de dispositivos del hogar mediante sensores y actuadores conectados a una red local o a internet.
Permite gestionar iluminación, temperatura, seguridad y más desde una interfaz gráfica o web.

---

## ⚙️ Características

- 💡 Control remoto de luces, ventiladores y otros dispositivos eléctricos.
- 🌡️ Monitoreo de temperatura, humedad y luminosidad.
- 🔐 Sistema de seguridad con detección de movimiento.
- 📱 Panel web o CLI para visualizar datos y enviar comandos.
- 📊 Registro de datos en una base local o en la nube.
- 🔊 Notificaciones mediante correo o Telegram.

---

## 🧩 Arquitectura del Proyecto

El sistema se divide en los siguientes módulos:

1. **Sensores y Actuadores:** Controlados mediante GPIO (si se usa Raspberry Pi) o comunicación serial (si se usa Arduino).
2. **Backend (Python):** Contiene la lógica de automatización, conexión MQTT/HTTP y manejo de datos.
3. **Base de Datos:** Almacena los registros de sensores y eventos.
4. **Interfaz de Usuario:** Puede ser una app Flask o FastAPI para acceso web.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología |
|-------------|-------------|
| Lenguaje | Python 3.10+ |
| Framework Web | Flask o FastAPI |
| Comunicación IoT | MQTT (paho-mqtt) o HTTP (requests) |
| Base de Datos | SQLite / Firebase / MySQL |
| Hardware | Raspberry Pi / ESP32 / Arduino |
| Librerías Clave | RPi.GPIO, paho-mqtt, flask, requests, sqlite3 |

---

## 🧱 Estructura del Proyecto

```bash
casa-domotica/
│
├── sensors/
│ ├── temperature_sensor.py
│ ├── motion_sensor.py
│ └── light_sensor.py
│
├── actuators/
│ ├── relay_controller.py
│ └── led_controller.py
│
├── server/
│ ├── app.py # Servidor Flask principal
│ └── routes.py
│
├── database/
│ └── db_handler.py
│
├── utils/
│ └── notifier.py
│
├── main.py # Punto de entrada del sistema
└── requirements.txt

# 1. Clonar el repositorio
git clone https://github.com/usuario/casa-domotica-python.git

# 2. Entrar al directorio
cd casa-domotica-python

# 3. Crear entorno virtual
python -m venv venv
source venv/bin/activate # En Linux/Mac
venv\Scripts\activate # En Windows

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar variables de entorno (opcional)
# Ejemplo (.env):
# MQTT_BROKER=broker.hivemq.com
# DB_PATH=./database/domotica.db

# 6. Ejecutar la aplicación
python main.py