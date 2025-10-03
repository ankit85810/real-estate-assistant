# 🏠 Real Estate Assistant (RAG-powered Tool)

This project is a **Real Estate Assistant** ([link](https://real-estate-assistant.streamlit.app/)) that allows users to provide real estate-related links, scrape their content, store the information in a vector database, and then ask natural language questions about the scraped data.  

It uses **LangChain**, **Hugging Face embeddings**, **ChromaDB**, and **Groq’s LLMs** to perform Retrieval-Augmented Generation (RAG). The frontend is powered by **Streamlit**.

---

## 🚀 Features
- Scrapes content from given URLs (e.g., real estate news, mortgage reports).
- Splits documents into manageable chunks.
- Stores the processed data in a persistent **Chroma vector store**.
- Allows you to ask **questions** about the documents.
- Provides **answers with sources**.
- User-friendly **Streamlit UI**.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ankit85810/real-estate-assistant.git
cd real-estate-assistant
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the project root directory and add:
```env
GROQ_API_KEY=your_groq_api_key_here
```

You can obtain your Groq API key from [Groq](https://groq.com/).

---

## ▶️ Usage

### Run the Streamlit app:
```bash
streamlit run main.py
```

1. Enter one or more URLs in the sidebar.
2. Click **Process URLs** to scrape and store the documents.
3. Enter a question in the text box.
4. Get answers with **sources**.

---

## 📂 Project Structure
```
real-estate-assistant/
│── rag.py        # Backend logic (scraping, embeddings, vector store, LLM QA)
│── main.py       # Streamlit frontend
│── requirements.txt
│── README.md
│── .env          # API keys (not included in repo)
│── resources/    # Persistent Chroma vector store
```

---

## ⚙️ Tech Stack
- **LangChain** – Orchestration framework
- **Chroma** – Vector store
- **Groq (LLaMA-3.3-70B)** – LLM for answering questions
- **Hugging Face** – Embedding model (`Alibaba-NLP/gte-base-en-v1.5`)  # you may use different model if it is not available
- **Streamlit** – Web interface
- **Python-dotenv** – Environment variable management

---

## ✅ Example

Example question after processing links:
```
Tell me what was the 30 year fixed mortgage rate along with the date?
```

The system will provide an **answer + sources** based on the scraped articles.

---

## 📌 Future Improvements
- Add support for **multiple embedding models**.
- Implement **chat history memory**.
- Support **PDF/CSV uploads** in addition to URLs.
- Dockerize the app for easier deployment.

---

## 👨‍💻 Author
Developed as a **Real Estate RAG Assistant** demo project.
