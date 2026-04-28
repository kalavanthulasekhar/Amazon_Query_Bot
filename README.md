# 🤖 Amazon RAG Chatbot (LangChain + Gemini + FAISS)

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) Chatbot** built using **LangChain, Google Gemini API, and FAISS Vector Database**.

The chatbot answers user queries **only based on provided data**, ensuring accurate and context-based responses instead of general AI knowledge.

---

## 🚀 Features

* 🔍 **RAG Architecture** (Retrieval + Generation)
* 🧠 Uses **Google Gemini API** for intelligent responses
* 📚 **FAISS Vector Database** for fast similarity search
* 📄 Reads data from external file (`docs.txt`)
* 💬 Interactive **Streamlit Chat UI**
* 🔌 Flask API for backend communication
* ❌ Prevents hallucination (answers only from data)

---

## 🏗️ Project Structure

```
Amazon_Chat_Bot/
│
├── rag_core.py        # RAG logic (retrieval + generation)
├── api.py             # Flask backend API
├── app.py             # Streamlit frontend UI
├── data/
│   └── docs.txt       # Knowledge base
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd Amazon_Chat_Bot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Get your Gemini API key from Google AI Studio and set it in your code:

```python
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
```

---

## ▶️ Run the Project

### Step 1: Start Flask API

```bash
python api.py
```

### Step 2: Start Streamlit UI

```bash
python -m streamlit run app.py
```

### Step 3: Open in Browser

```
http://localhost:8501
```

---

## 📄 Knowledge Base

The chatbot reads data from:

```
data/docs.txt
```

Example content:

* Amazon return policy
* Order tracking steps
* Account login instructions
* Prime membership details
* Customer support info

---

## 🧠 How It Works

1. User enters a query
2. Query is converted into embeddings
3. FAISS retrieves relevant documents
4. Gemini API generates answer using context
5. Response is returned to UI

---

## 📊 Technologies Used

* Python 🐍
* LangChain
* Google Gemini API
* FAISS
* Streamlit
* Flask

---

## 🎯 Use Cases

* Customer Support Chatbot
* FAQ Automation
* E-commerce Assistant
* Knowledge Base Search

---

## ⚠️ Limitations

* Depends on quality of input data
* Requires API key
* Limited by small dataset (can be expanded)

---

## 🚀 Future Improvements

* 📄 PDF Upload Support
* 🎤 Voice Assistant
* 🌐 Deployment (Render / AWS)
* 🎨 Advanced UI (ChatGPT-style)
* 🔐 User Authentication

---

## 👨‍💻 Author

**Kalavanthula Sekhar**
Sanskriti University

---

## 📜 License

This project is for educational purposes.
