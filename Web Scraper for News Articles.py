import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h3')
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.get_text(strip=True)}")

get_headlines('https://www.bbc.com/news')
