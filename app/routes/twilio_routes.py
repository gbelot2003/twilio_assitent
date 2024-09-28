from flask import request, jsonify
from app.services.openai_service import OpenAIService

def configure_twilio_routes(app):
    openai_service = OpenAIService()

    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():
        
        # Obtener el mensaje de Twilio
        message_body = request.form.get('Body')
        from_number = request.form.get('From')

        print(f"API: {message_body} || From: {from_number}")

         # Generar respuesta utilizando los fragmentos relevantes
        response = openai_service.generate_response(message_body)

        # Devolver la respuesta a Twilio
        return jsonify({"message": response})