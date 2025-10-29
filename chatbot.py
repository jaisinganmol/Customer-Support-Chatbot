import os
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain import ConversationBufferMemory

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
faiss_store = FAISS.load_local("embeddings/faq_index", embeddings)
retriever = faiss_store.as_retriever(search_kwargs={"k": 5})

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.4)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

def get_answer(query: str):
    response = qa_chain({"question": query})
    return response["answer"]
