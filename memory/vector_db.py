# memory/vector_db.py
# Retrieval-Augmented Generation (RAG) using ChromaDB

import os
import chromadb

class LongTermKnowledgeBase:
    def __init__(self):
        # Creates a local database folder to store massive documents forever
        db_path = "./generated_assets/.chroma_vault"
        os.makedirs(db_path, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="ctrl_master_knowledge")

    def ingest_document(self, doc_id: str, content: str):
        """Saves massive text data (codebases, pitch decks) into the vector matrix."""
        try:
            self.collection.add(
                documents=[content],
                ids=[doc_id]
            )
            return f"✅ Document '{doc_id}' successfully assimilated into Deep Memory."
        except Exception as e:
            return f"⚠️ Vector Ingestion Failed: {str(e)}"

    def search_knowledge(self, query: str, top_results: int = 1) -> str:
        """Searches the entire database in milliseconds for relevant facts."""
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_results
            )
            
            if results['documents'] and results['documents'][0]:
                # Combine the top results into a single context string
                return "\n---\n".join(results['documents'][0])
            return ""
        except Exception:
            return ""

# Instantiate the global knowledge base
knowledge_base = LongTermKnowledgeBase()
