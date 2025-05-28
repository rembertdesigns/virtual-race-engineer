# 🏎️ Virtual Race Engineer Assistant

An AI-powered assistant that lets users ask questions about Formula 1 races, drivers, and strategies — powered by LangChain + OpenAI + Streamlit. Built for RAG-style (retrieval-augmented generation) responses from official documents and race PDFs.

---

## 🚀 Features

- 🧠 Ask natural language questions about F1
- 📄 Retrieve answers from FIA documents and race summaries
- ⚡ Built with LangChain, FAISS, OpenAI, and Streamlit
- 🔧 Designed as a portfolio piece for ML/AI engineering roles

---

## 📁 Project Structure

```bash
virtual-race-engineer/
├── app/ # Streamlit frontend
│ └── main.py
├── data/ # Store your race PDFs here
├── rag/ # Ingest + RAG pipeline
│ ├── ingest.py # Turns PDFs into vector store
│ └── qa_chain.py # Handles LLM-based Q&A
├── requirements.txt # Dependencies
├── .env # API keys (not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/virtual-race-engineer.git
   cd virtual-race-engineer

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key
Create a `.env` file:
```bash
OPENAI_API_KEY=your-key-here
```
4. Add race PDFs
Place FIA documents or race summaries into the `/data` folder.

5. Ingest PDFs into vector DB
```bash
python rag/ingest.py
```
6. Run the Streamlit app
```bash
streamlit run app/main.py
```

---

## 🛠️ Roadmap

 - Add voice input via Whisper or streamlit-mic
 - Summarize strategy by team (contextual)
 - Track prompt history in-session
 - Deploy to Streamlit Cloud

---

## 📣 Credit & Inspiration

Built with:

- LangChain
- OpenAI GPT-4
- FAISS
- Streamlit

---

## 📌 Status

Currently in early development — core components scaffolded and ready for PDF ingestion + Q&A testing.

