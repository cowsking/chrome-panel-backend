from flask import Blueprint, request
import requests
send = Blueprint('send', __name__, url_prefix="/send")
from datetime import datetime

@send.post('/text')
def send_text():
    

            
    return "send"



    