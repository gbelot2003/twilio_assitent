from openai import OpenAI
from dotenv import load_dotenv
from app.services.contacto_service import ContactoService
import os


# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessageService:
    def handle_request(self, prompt, user_id):
        print(f"Usuario: {prompt}")

        if self.check_phone_user(user_id):
            print("Tiene un contacto en la base de datos.")
        else:
            print("No se ha encontrado el usuario en la base de datos.")

        messages = []

        messages.append({"role": "user", "content": prompt})

        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=450, temperature=0.1  # type: ignore
        )

        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

        print(f"GPT: {respuesta_modelo}")

        return respuesta_modelo
    
    def check_phone_user(self, user_id):
        contacto = ContactoService.obtener_contacto_por_telefono(telefono=user_id)

        if contacto is None:
            return False
        else:
            return True