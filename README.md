
# 🌍 FoodTradeGPT – Multilingual Export Regulations Assistant

FoodTradeGPT is an AI-powered assistant that helps users understand **food export regulations across countries** using natural language. It uses Retrieval-Augmented Generation (RAG) to provide accurate, structured, and multilingual responses.

---

## 🚀 Overview

Exporting food products involves complex legal requirements, certifications, and compliance rules that vary across countries. FoodTradeGPT simplifies this by allowing users to ask questions and receive clear, structured answers instantly.

The system ingests country-specific regulations (PDF/JSON), converts them into embeddings, and enables semantic search via a chatbot interface.

---

## ✨ Features

* 🌐 Multilingual support (Indian languages via Sarvam AI)
* 📄 Country-specific export regulations
* 🤖 AI-powered chatbot interface
* 🔍 Semantic search using vector embeddings (ChromaDB)
* ⚡ Lightweight backend using Flask
* 📊 Structured knowledge base (JSON)

---

## 🧠 How It Works

1. Regulatory data (PDF/JSON) is ingested
2. Text is split into smaller chunks
3. Chunks are converted into embeddings using sentence-transformers
4. Stored in ChromaDB (vector database)
5. User query → similarity search retrieves relevant context
6. LLM generates structured answer
7. Response is translated into the user’s language

---

## 🏗️ Tech Stack

* Python
* Flask
* LangChain
* ChromaDB
* Sentence Transformers
* Sarvam AI API
* HTML / CSS / JavaScript

---

## 📂 Project Structure

```bash
FoodTradeGPT/
│
├── export_ai_backend.py     # Main backend (Flask + RAG)
├── index.html               # Chatbot UI
├── script.js                # Frontend logic (if applicable)
├── style.css                # Styling (if applicable)
│
├── data/                    # Country regulation data (JSON)
│   ├── australia.json
│   ├── china.json
│   └── ...
│
├── vectorstore/             # ChromaDB storage
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FoodTradeGPT.git
cd FoodTradeGPT
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set environment variables

```bash
SARVAM_API_KEY=your_api_key_here
```

---

### 4. Run backend server

```bash
python export_ai_backend.py
```

---

### 5. Open frontend

Open `index.html` in your browser

---

## 📸 Demo

*Add screenshots or demo video link here*

---

## 🧪 Example Query

```text
What documents are required to export food to Australia?
```

👉 Output includes:

* Required documents
* Certifications
* Compliance requirements
* Key regulations

---

## 🚀 Future Improvements

* Add more countries and datasets
* Real-time regulation updates
* Export opportunity scoring system
* Deployment on cloud (AWS / Render)
* Improved UI/UX

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

MIT License
