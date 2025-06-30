# from data import extract_text
# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# results = extract_text()  # results = list of dicts
# for item in results:
#     text = item["text"]
#     embedding_vector = embeddings.embed_query(text)  # ✅ text ke liye embed_query
#     print(f"File: {item['filename']} | Page: {item['page']} | Embedding length: {len(embedding_vector)}")





# from data import extract_tables

# table_embeddings = []
# for item in extract_tables():
#     text = '\n'.join([' | '.join(row) for row in item["table_data"]])
#     emb = embeddings.embed_query(text)  # 🔑 Use embeddings, not embedding_model

#     table_embeddings.append({
#         "filename": item["filename"],
#         "page": item["page"],
#         # "table_index": item["table_index"],
#         "embedding": emb
#     })

#     print(f"File: {item['filename']} | Page: {item['page']} | Embedding Length: {len(emb)}")

from data import extract_text, extract_tables
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def embed_data():
    """Embeds for text data"""
    results = extract_text()
    embeddings = []
    for item in results:
        embeddings.append({
            "filename": item["filename"],
            "page": item["page"],
            "embedding": embedding_model.embed_query(item["text"])
        })
    return embeddings


def embed_tables():
    """Embeds for table data"""
    results = extract_tables()
    embeddings = []
    for item in results:
        table_text = '\n'.join([' | '.join(str(row) for row in item["table_data"]if row is not None)])
        embeddings.append({
            "filename": item["filename"],
            "page": item["page"],
            "embedding": embedding_model.embed_query(table_text)
        })
    return embeddings
