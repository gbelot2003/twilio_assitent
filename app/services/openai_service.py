import os
from openai import OpenAI
from dotenv import load_dotenv
from app.models.conversacion_model import Conversacion
from extensions import db

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    def __init__(self): 
        pass

    def generate_response(self, prompt, user_id):
        return self.handle_request(prompt, user_id)
    
    def handle_request(self, prompt, user_id):

        print(f"Usuario: {prompt}")

        messages = []

        messages.append({"role": "user", "content": prompt})

        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=450, temperature=0.1  # type: ignore
        )

        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

        print(f"GPT: {respuesta_modelo}")

        # Guardar la conversación en la base de datos
        self.guardar_conversacion(prompt, user_id, respuesta_modelo)

        return respuesta_modelo
    
    
    def guardar_conversacion(self, prompt, user_id, respuesta_modelo):
        conversation = Conversacion(user_message=prompt, bot_response=respuesta_modelo, user_id=user_id)
        db.session.add(conversation)
        db.session.commit()