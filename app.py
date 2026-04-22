from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
from utils.pdf_reader import extract_text_from_pdf
from utils.chunker import chunk_text
from utils.embedder import create_embeddings
from utils.vector_db import save_to_faiss
from utils.vector_db import search_chunks
from utils.llm import get_answer

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("vectorstore", exist_ok=True)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Upload PDF
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    # AI pipeline
    text = extract_text_from_pdf(filepath)
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    save_to_faiss(embeddings, chunks)

    return jsonify({
        "message": "PDF uploaded & indexed successfully"
    })


# Ask Query (temporary dummy)
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    query = data.get("query")

    relevant_chunks = search_chunks(query)

    context = "\n\n".join(relevant_chunks)

    answer = get_answer(context, query)

    return jsonify({
        "question": query,
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)