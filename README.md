# Twilio Assistant with OpenAI

Este repositorio contiene una aplicación Flask que integra un servicio de chatbot utilizando OpenAI y Twilio. La aplicación permite recibir mensajes de usuarios a través de Twilio, procesarlos utilizando OpenAI, y almacenar las conversaciones en una base de datos SQLite. Además, la aplicación incluye funcionalidades para extraer nombres de usuarios y almacenar información de contacto.

## Estructura del Proyecto

El proyecto está organizado en varios módulos y servicios:

```
twilio_assitent/
│
├── app/
│   ├── models/
│   │   ├── contacto_model.py
│   │   ├── conversacion_model.py
│   │
│   ├── modules/
│   │   ├── nombre_extractor.py
│   │   ├── embedding_processing.py
│   │   ├── pdf_processing.py
│   │
│   ├── routes/
│   │   ├── routes.py
│   │   ├── twilio_routes.py
│   │   ├── wsi_routes.py
│   │
│   ├── services/
│   │   ├── contacto_service.py
│   │   ├── conversaciones_service.py
│   │   ├── nombre_service.py
│   │   ├── openai_service.py
│   │   ├── system_message_service.py
│   │   ├── chromadb_service.py
│   │
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── post_simulator.html
│
├── config.py
├── extensions.py
├── main.py
├── README.md
└── static/
    └── style.css
```

## Descripción de Archivos

### `main.py`

Punto de entrada de la aplicación. Configura la aplicación Flask, inicializa la base de datos, y configura las rutas.

### `config.py`

Contiene la configuración de la aplicación, incluyendo la clave secreta y la URI de la base de datos.

### `extensions.py`

Inicializa la extensión SQLAlchemy para la base de datos.

### `app/routes/routes.py`

Configura las rutas principales de la aplicación, incluyendo las rutas para Twilio y WSI (Web Service Interface).

### `app/routes/twilio_routes.py`

Define la ruta para manejar los webhooks de Twilio, utilizando OpenAI para generar respuestas.

### `app/routes/wsi_routes.py`

Define la ruta para enviar mensajes simulados a través de una interfaz web.

### `app/modules/nombre_extractor.py`

Contiene la clase `NombreExtractor` para extraer nombres de texto utilizando expresiones regulares.

### `app/modules/embedding_processing.py`

Procesa y obtiene embeddings de fragmentos de texto utilizando OpenAI.

### `app/modules/pdf_processing.py`

Extrae texto de archivos PDF y lo divide en fragmentos más pequeños para evitar los límites de la API.

### `app/models/contacto_model.py`

Define el modelo `Contacto` para almacenar información de contacto en la base de datos.

### `app/models/conversacion_model.py`

Define el modelo `Conversacion` para almacenar las conversaciones entre usuarios y el bot.

### `app/services/contacto_service.py`

Contiene la lógica para gestionar la creación, actualización, y eliminación de contactos.

### `app/services/conversaciones_service.py`

Contiene la lógica para gestionar la creación y eliminación de conversaciones.

### `app/services/nombre_service.py`

Utiliza `NombreExtractor` para detectar y almacenar nombres de usuarios.

### `app/services/openai_service.py`

Integra la API de OpenAI para generar respuestas a partir de mensajes de usuarios.

### `app/services/system_message_service.py`

Maneja las solicitudes de mensajes del sistema, utilizando OpenAI para generar respuestas.

### `app/services/user_info_service.py`

Gestiona la información del usuario, como el nombre y el email.

### `app/services/chromadb_service.py`

Inicializa y gestiona la base de datos ChromaDB para almacenar y buscar embeddings de texto.

### `app/templates/base.html`

Plantilla base para las páginas HTML de la aplicación.

### `app/templates/index.html`

Página principal de la aplicación.

### `app/templates/post_simulator.html`

Interfaz para simular envíos de mensajes a través de una URL.

### `static/style.css`

Archivos de estilos CSS para la aplicación.

## Guía de Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

### Pasos de Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/gbelot2003/twilio_assitent.git
   cd twilio_assitent
   ```

2. **Crear un Entorno Virtual (Opcional pero Recomendado)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Variables de Entorno**

   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```env
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_NUMBER=your_twilio_number
   ```

5. **Ejecutar la Aplicación**

   ```bash
   flask run
   ```

   La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

### Interfaz Web

1. **Acceder a la Interfaz Web**

   Abre tu navegador y ve a `http://127.0.0.1:5000/`.

2. **Simular Mensajes**

   Utiliza la interfaz en `http://127.0.0.1:5000/post_simulator` para simular envíos de mensajes a través de una URL.

### Integración con Twilio

1. **Configurar Webhook en Twilio**

   Configura el webhook en tu cuenta de Twilio para apuntar a `http://your_server_ip:5000/api/twilio`.

2. **Enviar Mensajes**

   Envía mensajes a tu número de Twilio configurado para recibir respuestas generadas por OpenAI.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

