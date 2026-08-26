from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
## Exmaple Usage
if __name__ == "__main__":
    # docs = load_all_documents("data") # for the first time only
    # chunks = EmbeddingPipeline().chunk_documents(docs) # documents -> chunks
    # chunkvectors = EmbeddingPipeline().embed_chunks(chunks) # chunks -> embedding
    # print(chunkvectors)
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs) # only when you have new documents then use it
    store.load()
    # print(store.query("What is Agentic Pharma Covigilence?", top_k=3))
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)