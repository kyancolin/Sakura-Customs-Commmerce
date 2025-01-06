import requests
from bs4 import BeautifulSoup

# URL van de pagina die je wilt scrapen
url = 'https://www.alternate.nl/CPUs'

# Haal de pagina op
response = requests.get(url)

# Controleer of de aanvraag succesvol was
if response.status_code == 200:
    # Maak een BeautifulSoup-object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Zoek naar de gegevens die je wilt extraheren
    for product in soup.find_all('div', class_='product-item'):
        name = product.find('h2', class_='product-name').text
        price = product.find('span', class_='product-price').text
        print(f'Product: {name}, Price: {price}')
else:
    print('Error fetching the page')

