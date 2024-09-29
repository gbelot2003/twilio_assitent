# app/routes/twilio_routes.py

from flask import request, jsonify
from app.services.openai_service import OpenAIService

def configure_twilio_routes(app):
    openai_service = OpenAIService()

    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():
        
        # Obtener datos desde mensajes de API
        message_body = request.form.get('Body')
        from_number = request.form.get('From')

        # Generar la respuesta usando OpenAIService
        response = openai_service.generate_response(message_body, from_number)

        # Devolver la respuesta a Twilio
        return jsonify({"message": response})
        
        