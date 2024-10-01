# app/modules/address_recognition.py
import re

class AddressExtractor:
    """
    Clase encargada de extraer direcciones de los mensajes del usuario.
    """
    def __init__(self):
        # Patrón de regex para detectar la dirección
        self.pattern = re.compile(r"(dirección|ubicación)\s+(de\s+)?(.+)", re.IGNORECASE)

    def extract(self, text: str) -> str:
        """
        Extrae la dirección del mensaje usando expresiones regulares.
        :param text: Mensaje del usuario.
        :return: Dirección extraída o None si no se encuentra.
        """
        match = self.pattern.search(text)
        if match:
            # Devuelve solo la parte que creemos que es la dirección
            return match.group(3).strip()
        return None
