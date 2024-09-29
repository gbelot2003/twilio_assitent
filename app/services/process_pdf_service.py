# app/services/process_pdf_service.py

from app.modules.pdf_processing import extract_text_from_pdf, split_text_into_chunks
from app.modules.embedding_processing import get_embedding_for_chunk
from app.services.chromadb_service import store_chunks_in_chromadb

def process_pdf(pdf_path):
    try:
        text = extract_text_from_pdf(pdf_path)
        chunks = split_text_into_chunks(text)
        chunks_with_embeddings = [(chunk, get_embedding_for_chunk(chunk)) for chunk in chunks]
        store_chunks_in_chromadb(chunks_with_embeddings, pdf_path)
    except Exception as e:
        print(f"Error procesando el PDF {pdf_path}: {e}")