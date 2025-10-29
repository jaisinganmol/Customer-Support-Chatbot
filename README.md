***

# Customer-Support-Chatbot

A production-grade, Retrieval-Augmented Generation (RAG) chatbot platform for customer support, built with Python, LangChain, FAISS, OpenAI GPT-4, Streamlit, and FastAPI.  
Deliver instant, relevant answers, automate ticketing, and deeply integrate with your support workflow.

***

## Features

- **RAG pipeline:** Delivers highly accurate answers by combining search and GPT-4 generation.
- **Contextual multi-turn dialogue:** Maintains full chat history for natural conversations.
- **Beautiful chat interface:** Streamlit-driven, real-time, and easy for both customers and agents to use.
- **FastAPI backend:** Secure, modular, and ready to connect with your existing CRM or help desk.
- **Automated CRM ticketing:** Triages and escalates complex issues when needed.
- **Plug-and-play knowledge base:** Ingest documents of any size and update easily with zero downtime.

***

## Getting Started

### 1. Install Prerequisites

- Python 3.9+
- `pip`, `git`
- [Optional] `pdfminer.six` if using PDFs

### 2. Setup Project

```sh
git clone <your-repo-url> Customer-Support-Chatbot
cd Customer-Support-Chatbot
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


### 3. Configure Environment

Create `.env` and specify:

```env
OPENAI_API_KEY=your_openai_api_key
CRM_API_URL=https://crm.example.com/api
CRM_AUTH_TOKEN=your_crm_token
```


### 4. Add Knowledge Base Content

- Put FAQs and reference docs as `.txt` (or optional `.pdf`) files in `data/`
- Run the indexer:
  ```sh
  python run_once_index.py
  ```
- This builds a FAISS vector store in `embeddings/`

### 5. Launch Backend & Frontend

- **API backend:**  
  ```
  uvicorn api:app --reload
  ```
- **Chat UI:**  
  ```
  streamlit run app.py
  ```


Browse to the URL shown by Streamlit to start chatting!

***

## How It Works

1. Questions flow from the chat UI to your FastAPI backend.
2. Backend queries the vector index (FAISS) for the most relevant knowledge chunks.
3. GPT-4 (or compatible LLM) generates an answer using both the customer question and the retrieved context.
4. If escalation criteria are met, a new CRM ticket is created and the agent receives a notification.
5. All conversation history is preserved, so each reply understands previous turns.

***

## Project Structure

```text
.
├── app.py              # Streamlit UI
├── api.py              # FastAPI backend/API
├── chatbot.py          # Core RAG and ticketing logic
├── run_once_index.py   # One-time ingestion/indexing script
├── requirements.txt
├── .env
├── data/               # Put raw source files here
├── embeddings/         # Auto-generated FAISS vector index
```


***

## Configuration & Customization

- **Add or update docs:** Place files in `data/`, rerun `run_once_index.py`.
- **Tweak retrieval:** Adjust chunking, number of results (`k`), or the prompt template in `chatbot.py`.
- **Switch LLM providers:** Change the setup in `chatbot.py` for OpenAI GPT-4 or another API-compatible model.
- **Customize ticketing:** Edit CRM integration logic in `api.py` to match your workflows.
- **UI tweaks:** Update `app.py` for branding or UX improvements.

***

## Troubleshooting

- Missing integrations?  
  ```
  pip install langchain-community
  ```
- Errors importing modules?  
  Double-check import paths and Python version.
- Old or broken answers?  
  Rerun `python run_once_index.py` after updating content.
- API issues?  
  Check keys and endpoints in your `.env`.

***

## License

MIT License

***

## Credits

Powered by the open-source AI community and technologies including LangChain, OpenAI, Streamlit, FastAPI, and FAISS.

***
