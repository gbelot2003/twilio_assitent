# app/services/openai_service.py

from app.models.conversacion_model import Conversacion
from app.services.system_message_service import SystemMessageService
from extensions import db

class OpenAIService:
    def __init__(self): 
        self.system_message_service = SystemMessageService()

    def generate_response(self, prompt, user_id):
        return self.handle_request(prompt, user_id)
    
    def handle_request(self, prompt, user_id):

        # Manejador de mensajes
        respuesta_modelo = self.system_message_service.handle_request(prompt, user_id)
        
        # Devolver la respuesta generada por el modelo
        return respuesta_modelo
    
    
