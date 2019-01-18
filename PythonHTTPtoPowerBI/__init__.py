import logging
import json
import os
from datetime import datetime
import azure.functions as func
import requests

pbi_push_conn_str = os.environ['powerbi_push_connstring']

def main(req: func.HttpRequest) -> None:
    content = req.get_json()
    # alter content
    content['processed'] = datetime.utcnow().isoformat()
    r = requests.post(pbi_push_conn_str, data = json.dumps([content]))
