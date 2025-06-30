import chromadb
import os
import pickle
from embed import embed_data, embed_tables
from langchain_huggingface import HuggingFaceEmbeddings
import logging
#from chromadb.config import Settings

# Disable chromadb telemetry warnings
logging.getLogger("chromadb.telemetry").setLevel(logging.CRITICAL)

# Initialize ChromaDB client
client = chromadb.Client()
# Create collections
text_collection = client.get_or_create_collection("text_data")
table_collection = client.get_or_create_collection("table_data")

# ========= Load or generate text embeddings ===========
if os.path.exists("saved_text_embeddings.pkl"):
    print("📥 Loading saved text embeddings...")
    with open("saved_text_embeddings.pkl", "rb") as f:
        text_embeddings = pickle.load(f)
else:
    print("🔁 Generating text embeddings...")
    text_embeddings = embed_data()
    with open("saved_text_embeddings.pkl", "wb") as f:
        pickle.dump(text_embeddings, f)

# ========= Load or generate table embeddings ===========
if os.path.exists("saved_table_embeddings.pkl"):
    print("📥 Loading saved table embeddings...")
    with open("saved_table_embeddings.pkl", "rb") as f:
        table_embeddings = pickle.load(f)
else:
    print("🔁 Generating table embeddings...")
    table_embeddings = embed_tables()
    with open("saved_table_embeddings.pkl", "wb") as f:
        pickle.dump(table_embeddings, f)

# ========= Add to Chroma collections ===========
print(f"➕ Adding {len(text_embeddings)} text items to ChromaDB")
for i, item in enumerate(text_embeddings):
    text_collection.add(
        ids=[f"text-{i}"],
        embeddings=[item["embedding"]],
        metadatas=[{"filename": item["filename"], "page": item["page"]}],
        documents=["Text data"]
    )

print(f"➕ Adding {len(table_embeddings)} table items to ChromaDB")
for i, item in enumerate(table_embeddings):
    table_collection.add(
        ids=[f"table-{i}"],
        embeddings=[item["embedding"]],
        metadatas=[{
            "filename": item["filename"],
            "page": item["page"],
            "table_index": item.get("table_index", -1)
        }],
        documents=["Table data"]
    )

print("✅ Embeddings inserted into vector store.")
def retrieve_docs(query, top_k=3):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    query_embedding = embedding_model.embed_query(query)

    text_results = text_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    table_results = table_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return text_results, table_results