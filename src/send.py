from flask import Blueprint, request
import requests
send = Blueprint('send', __name__, url_prefix="/send")
from datetime import datetime

@send.post('/chat')
def send_chat():
    

            
    return "send"


@send.post('/tab')
def send_chat():
    # Get the tab ID and content from the request parameters
    tab_id = request.json['tab_id']
    content = request.json['content']
    

    # Return a response
    return ",".join([tab_id,content])


    