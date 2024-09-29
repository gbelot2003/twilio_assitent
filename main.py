# main.py

from flask import Flask
from flask_socketio import SocketIO
from flask_migrate import Migrate
from app.routes.routes import configure_routes
from app.services.process_pdf_service import process_pdf
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")

# Lista de rutas de archivos PDF
pdf_paths = [
    "files/encomiendas.pdf",
    # Agrega más rutas de archivos PDF aquí
]

# Procesar cada PDF al iniciar la aplicación
for pdf_path in pdf_paths:
    process_pdf(pdf_path)

# Configurar las rutas
configure_routes(app, socketio)

# Iniciar el servidor
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)