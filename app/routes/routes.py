# app/routes/routes.py

from flask import render_template, jsonify, request
from app.routes.twilio_routes import configure_twilio_routes
from app.routes.wsi_routes import configure_wsi_routes

def configure_routes(app, socketio):
    
    # Configurar las rutas de WSI y send_message
    configure_wsi_routes(app)

    configure_twilio_routes(app)

    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")
    
