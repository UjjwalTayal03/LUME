# LUME ✨

### AI-Powered PDF Question Answering System using RAG

LUME is an intelligent document understanding system that allows users to upload PDF files and ask natural language questions based on the uploaded content.

Instead of manually reading long documents, users can simply ask questions and receive context-grounded answers instantly.

LUME uses **Retrieval-Augmented Generation (RAG)** with semantic embeddings, vector search, and a Large Language Model (LLM) to provide accurate responses from the uploaded document.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🤖 Ask questions in natural language
* 🔍 Semantic search using embeddings
* 🧠 FAISS vector database for fast retrieval
* 💬 AI-generated answers grounded in document content
* ⚡ Fast and lightweight Flask backend
* 🎯 Handles unrelated questions gracefully
* 🖥️ Clean and simple UI

---

## 🧠 How It Works

LUME follows a **RAG (Retrieval-Augmented Generation)** pipeline:

### 1. PDF Upload

User uploads a PDF document.

### 2. Text Extraction

The system extracts raw text from the PDF using PyMuPDF.

### 3. Chunking

The extracted text is split into smaller chunks for better retrieval.

### 4. Embedding Generation

Each chunk is converted into vector embeddings using Sentence Transformers.

### 5. Vector Storage

Embeddings are stored inside FAISS for semantic similarity search.

### 6. Query Processing

When the user asks a question:

* The question is converted into embedding
* Relevant chunks are retrieved from FAISS
* Retrieved context is sent to the LLM API
* Final answer is generated strictly from document context

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### AI / NLP

* Sentence Transformers
* FAISS
* Retrieval-Augmented Generation (RAG)

### LLM API

* Groq API (Llama Model)

### PDF Processing

* PyMuPDF

### Frontend

* HTML
* CSS
* JavaScript

---

## 📁 Project Structure

```bash
LUME/
│── app.py
│── requirements.txt
│── .env
│
├── uploads/
├── vectorstore/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── utils/
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_db.py
│   └── llm.py
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repository-link>
cd LUME
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Project

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Sample Questions

After uploading a PDF, try:

* How many annual leaves are provided?
* Is remote work allowed?
* What are working hours?
* When are performance reviews conducted?

### ❌ Unrelated Query Example

**Q:** What is CEO salary?

### ✅ Expected Output

```
Information not found in document.
```

---

## 🎯 Use Cases

* 📚 Student Notes Assistant
* 🏢 Company Policy Q&A
* 📄 Resume / Report Understanding
* 📘 Research Paper Assistant
* ⚖️ Legal / Policy Search
* 📑 Internal Knowledge Base

---

## 🔥 Why LUME?

Traditional search systems rely on keyword matching.

LUME understands the meaning behind the question using semantic embeddings, retrieves the most relevant context, and generates a grounded response.

This makes answers:

* Smarter
* Faster
* More Accurate

---

## 📈 Future Enhancements

* 📂 Multiple PDF upload support
* 🧠 Chat history / memory
* 🌐 Cloud deployment
* 👥 User authentication
* 📊 Source citations
* 🖼️ OCR for scanned PDFs
* 🌍 Multi-language support
* 📱 Better responsive UI
* 📌 Confidence score
* 📎 Export answers/chat

---

## 🧠 Learning Outcomes

This project demonstrates practical understanding of:

* NLP Embeddings
* Semantic Search
* Vector Databases
* Retrieval-Augmented Generation
* LLM API Integration
* Flask Backend Development
* AI Product Architecture

---

## 👨‍💻 Author

**Ujjwal Tayal**

---

## ⭐ Final Note

LUME is a practical AI assistant for documents that combines modern NLP with real-world usability.

**Upload. Ask. Understand. ✨**
