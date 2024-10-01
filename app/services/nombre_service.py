# app/services/nombre_service.py

from app.modules.nombre_extractor import NombreExtractor
from app.modules.address_extractor import AddressExtractor

class NombreService:
    def __init__(self, user_info_service):
        self.nombre_extractor = NombreExtractor()
        self.user_info_service = user_info_service
        self.address_extractor = AddressExtractor()

    def detectar_y_almacenar_nombre(self, prompt):
        # Intentamos extraer el nombre del prompt
        nombre_detectado = self.nombre_extractor.extraer_nombre(prompt)
        
        if nombre_detectado:
            self.user_info_service.set_nombre(nombre_detectado)
            return nombre_detectado
        return None
    
    def detectar_y_almacenar_direccion(self, prompt):
        # Intentamos extraer la dirección del prompt
        direccion_detectada = self.address_extractor.extract(prompt)
        
        if direccion_detectada:
            self.user_info_service.set_address(direccion_detectada)
            return direccion_detectada
        return None
    
    