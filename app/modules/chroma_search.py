# app/modules/chroma_search.py

from app.services.chromadb_service import search_in_chromadb
from app.modules.embedding_processing import get_embedding_for_chunk

def buscar_fragmentos_relevantes(prompt):
    # Obtener el embedding del prompt
    query_embedding = get_embedding_for_chunk(prompt)
    
    # Buscar en ChromaDB los fragmentos más relevantes
    relevant_chunks = search_in_chromadb(query_embedding)
    
    # Incluir los fragmentos relevantes en el prompt
    if relevant_chunks:
        relevant_info = "\n".join(relevant_chunks)
        return {
            "role": "system",
            "content": f"Información relevante:\n{relevant_info}",
        }
    return None