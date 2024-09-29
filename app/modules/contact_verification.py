# app/modules/contact_verification.py

from app.services.contacto_service import ContactoService

def verificar_contacto(user_id):
    # Verificar si el usuario tiene un número de teléfono en la base de datos
    contacto = ContactoService.obtener_contacto_por_telefono(user_id)

    if not contacto:
        # Si no existe, crear un nuevo contacto con el número de teléfono
        contacto = ContactoService.crear_contacto(telefono=user_id)
        print(f"Nuevo contacto creado: {contacto.telefono}")
    else:
        # Si existe, extraer la información del contacto
        nombre = contacto.nombre
        direccion = contacto.direccion
        email = contacto.email
        print(f"Contacto encontrado: {nombre}, {direccion}, {email}")

    return contacto