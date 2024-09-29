# app/services/openai_service.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from app.models.conversacion_model import Conversacion
from app.services.system_message_service import SystemMessageService
from extensions import db

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    def __init__(self): 
        self.system_message_service = SystemMessageService()

    def generate_response(self, prompt, user_id):
        return self.handle_request(prompt, user_id)
    
    def handle_request(self, prompt, user_id):

        # Manejador de mensajes
        respuesta_modelo = self.system_message_service.handle_request(prompt, user_id)

        # Guardar la conversación en la base de datos
        self.guardar_conversacion(prompt, user_id, respuesta_modelo)

        # Devolver la respuesta generada por el modelo
        return respuesta_modelo
    
    
    def guardar_conversacion(self, prompt, user_id, respuesta_modelo):
        conversation = Conversacion(user_message=prompt, bot_response=respuesta_modelo, user_id=user_id)
        db.session.add(conversation)
        db.session.commit()

        