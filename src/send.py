from flask import Blueprint, request
import requests
send = Blueprint('send', __name__, url_prefix="/send")
from datetime import datetime
import json
from src.vectorstore import build_db

@send.post('/chat')
def send_chat():
    

            
    return "send"


@send.post('/tab')
def send_tab():
    # Create a dictionary with the tab ID and content
    tab_id = request.json['tab_id']
    content = request.json['content']
    
    build_db.store_faiss_db(tab_id=tab_id, content=content)
    # Create a dictionary with the tab ID and content
    response_data = {'tab_id': tab_id, 'content': content}

    # Convert the dictionary to JSON
    response_json = json.dumps(response_data)

  
    return response_json