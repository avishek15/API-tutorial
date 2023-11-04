import requests
from dotenv import load_dotenv
import os
import json

_ = load_dotenv()

if __name__ == '__main__':
    # newsapi_key = os.environ["NEWSAPI"]
    # response = requests.get(f"https://newsapi.org/v2/everything?q=keyword&apiKey={newsapi_key}")
    # # print(response.status_code)
    #
    # print(json.dumps(json.loads(response.text), indent=2))
    print(requests.get("http://localhost:8000/").text)
