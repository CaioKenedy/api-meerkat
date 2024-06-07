from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def scrape_site():
    url = "http://bianca.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    h1 = soup.h1.text

    return h1


@app.route('/conteudo')
def get_conteudo():
    # Chama a função de scraping para obter o conteúdo da página
    conteudo = scrape_site()
    return conteudo

if __name__ == '__main__':
    # Executa a aplicação Flask
    app.run(debug=True)
