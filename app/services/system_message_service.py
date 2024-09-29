# app/services/system_message_service.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from app.services.conversaciones_service import ConversacionService
from app.services.nombre_service import NombreService
from app.services.user_info_service import UserInfoService
from app.modules.contact_verification import verificar_contacto
from app.modules.chroma_search import buscar_fragmentos_relevantes
from app.modules.conversation_history import preparar_mensajes

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessageService:
    def __init__(self):
        self.nombre_service = NombreService(UserInfoService())

    def handle_request(self, prompt, user_id):
        try:
            print(f"Usuario: {prompt}")

            # Verificar si el usuario tiene un número de teléfono en la base de datos
            contacto = verificar_contacto(user_id)

            # Inicializar la variable nombre
            nombre = contacto.nombre if contacto else None

            # Preparar los mensajes con el historial de conversaciones y el nombre del usuario
            messages = preparar_mensajes(user_id, nombre, self.nombre_service)

            # Buscar fragmentos relevantes en ChromaDB
            relevant_info = buscar_fragmentos_relevantes(prompt)
            if relevant_info:
                messages.append(relevant_info)

            # Agregar el mensaje actual del usuario
            messages.append({"role": "user", "content": prompt})

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
        except Exception as e:
            print(f"Error en handle_request: {e}")
            return "Lo siento, ha ocurrido un error al procesar tu solicitud."