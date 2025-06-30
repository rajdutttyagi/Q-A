Q‑A 🚀

A question‑answering engine built with a lightweight LLM pipeline. This project ingests PDFs, images, and web data, indexes them semantically in ChromaDB, and uses Groq‑powered LLM components to transform queries, generate responses, and validate output—all on free or open‑source infrastructure.

🔍 Features

📂 Multimodal PDF ingestion:-

Extracts text, tables, and embedded images using PyMuPDF (fitz).

🖼 Image captioning + embedding:-

Converts PDF‑embedded images into captions, then embeds via open‑source vision‑language models.

⚙️ Semantic indexing with ChromaDB:-

Stores and searches unified embeddings from text, tables, and image captions.

🔎 Context-aware query routing:-

Classifies queries to either search the vector DB or trigger a fallback web search.

🤖 Groq‑inference for QA pipeline:-

Uses Groq's open‑weight LLMs for:

Query reformulation

Answer generation based on retrieved context

Relevancy and hallucination checks

🌐 Web‑search fallback:-

Retrieves live data when vector results are insufficient.

🛠 Modular and deployable:-

Easily swap in new LLMs or external APIs with minimal refactoring.

⚙️ Tech Stack

Python

PyMuPDF (fitz) – PDF extraction

Hugging Face + Sentence Transformers – embeddings

ChromaDB – vector store

Open‑source Vision Models – image captioning

Groq – LLM inference (transform, generate, validate)

(Optional) Flask/FastAPI – API or UI layer

🧠 Architecture Overview

[PDF/Images] → Extract (text, tables, images)
     ↓
 Captioning + Embedding → ChromaDB vector store
     ↓
[User Query] → Classifier (LLM): Retrieval vs Fallback
     ↓
  ┌────────────┐        ┌──────────────────────────┐
  │ Retrieval  │        │  Web Search Fallback     │
  │ (ChromaDB) │        └──────────────────────────┘
  └────────────┘               ↓
       ↓                 Contextual Retrieval
Query + Context → LLM (Groq):
  • Reformulate query  
  • Generate answer  
  • Validate output  
       ↓
   API Response → JSON / UI

🛠️ Customization Tips

Swap ChromaDB for another vector DB (e.g. Weaviate, Pinecone) by rewriting the ingestion and retrieval modules.

Replace Groq LLM calls with any open‑weight or hosted LLM; interfaces are encapsulated in llm_client.py.

Extend ingestion to support DOCX, CSV, or HTML files.

Enhance image captioning by using more advanced models (e.g. BLIP‑2, GPT+vision).

🏷️ LICENSE

This project is released under the MIT License — feel free to reuse and adapt it.

✉️ Contact

Questions, suggestions, or feedback? Open an issue or email [rdtyagi05@gmail.com].
