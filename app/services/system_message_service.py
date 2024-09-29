# app/services/system_message_service.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from app.services.contacto_service import ContactoService
from app.services.conversaciones_service import ConversacionService
from app.services.nombre_service import NombreService
from app.services.user_info_service import UserInfoService
from app.modules.contact_verification import verificar_contacto
from app.modules.chroma_search import buscar_fragmentos_relevantes

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

            # Recuperar el historial de conversaciones del usuario
            chat_history = ConversacionService.obtener_conversaciones_por_user_id(user_id)

            # Crear la lista de mensajes para enviar a OpenAI
            messages = []

            # Agregar el historial de conversaciones al prompt
            for conversacion in chat_history:
                messages.append({"role": "user", "content": conversacion.user_message})
                messages.append({"role": "assistant", "content": conversacion.bot_response})

            # Si el contacto tiene un nombre, usarlo en la conversación
            if nombre:
                messages.append({"role": "system", "content": f"El usuario se llama {nombre}."})
            else:
                # Si no tiene nombre, intentar extraerlo del prompt
                nombre_detectado = self.nombre_service.detectar_y_almacenar_nombre(prompt)
                if nombre_detectado:
                    messages.append({"role": "system", "content": f"El usuario se llama {nombre_detectado}."})
                    # Actualizar el contacto con el nombre detectado
                    ContactoService.actualizar_contacto(contacto.id, nombre=nombre_detectado)

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