# app/services/system_message_service.py

from openai import OpenAI
from dotenv import load_dotenv
from app.services.contacto_service import ContactoService
from app.services.conversaciones_service import ConversacionService
import os


# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessageService:
    def handle_request(self, prompt, user_id):
        print(f"Usuario: {prompt}")

        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = ContactoService.obtener_contacto_por_telefono(user_id)

        if not contacto:
            # Si no existe, crear un nuevo contacto con el número de teléfono
            contacto = ContactoService.crear_contacto(telefono=user_id)
            print(f"Nuevo contacto creado: {contacto.telefono}")

        messages = []

        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=450, temperature=0.1  # type: ignore
        )

        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

        print(f"GPT: {respuesta_modelo}")

         # Guardar la conversación en la base de datos
        ConversacionService.crear_conversacion(prompt, respuesta_modelo, user_id)

        return respuesta_modelo

        
        