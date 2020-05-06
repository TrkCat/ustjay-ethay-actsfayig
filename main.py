import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_response_url(url, input_data):
    response = requests.post(url, data=input_data)

    return response.url


@app.route('/')
def home():
    fact = get_fact().strip()
    url = get_response_url('https://hidden-journey-62459.herokuapp.com/piglatinize/', {'input_text': fact})
    
    return ('<a href={0}>{0}</a>'.format(url))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

