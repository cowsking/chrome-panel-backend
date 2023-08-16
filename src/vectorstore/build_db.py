from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from bs4 import BeautifulSoup
import requests


DATA_PATH = "vectorstore"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def store_faiss_db(tab_id, content):
    # Store HTML content to FAISS vectorstore
    response = requests.get(content)
    html_content = response.text
    
    
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                    model_kwargs={'device': 'cpu'})

    vectorstore = FAISS.from_documents(text, embeddings)
    vectorstore.save_local(f'vectorstore/{tab_id}')
    