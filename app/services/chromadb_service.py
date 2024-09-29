# app.services.chromadb_service.py
import chromadb

# Inicializar ChromaDB con SQLite
chroma_client = chromadb.PersistentClient(path="chromadb")

def store_chunks_in_chromadb(chunks_with_embeddings, pdf_path, collection_name="pdf_collection"):
    """Vectoriza y almacena fragmentos de texto en ChromaDB."""
    collection = chroma_client.get_or_create_collection(collection_name)
    
    for i, (chunk, embedding) in enumerate(chunks_with_embeddings):
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{pdf_path}_chunk_{i}"]
        )
        print(f"Fragmento {i+1} del PDF {pdf_path} almacenado en ChromaDB.")

def search_in_chromadb(query_embedding, collection_name="pdf_collection"):
    """Busca en ChromaDB utilizando el embedding de una consulta."""
    collection = chroma_client.get_collection(collection_name)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3  # Número de resultados a devolver
    )
    if results['documents']:
        # Asegurarse de que 'documents' es una lista de cadenas de texto
        relevant_chunks = [doc[0] for doc in results['documents']]
        return relevant_chunks
    else:
        return ["No se encontró información relevante."]