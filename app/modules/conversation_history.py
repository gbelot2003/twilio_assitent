# app/modules/conversation_history.py

from app.services.conversaciones_service import ConversacionService
from app.services.contacto_service import ContactoService

def preparar_mensajes(user_id, nombre=None, nombre_service=None):
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
        if nombre_service:
            nombre_detectado = nombre_service.detectar_y_almacenar_nombre(prompt)
            if nombre_detectado:
                messages.append({"role": "system", "content": f"El usuario se llama {nombre_detectado}."})
                # Actualizar el contacto con el nombre detectado
                ContactoService.actualizar_contacto(contacto.id, nombre=nombre_detectado)

    return messages