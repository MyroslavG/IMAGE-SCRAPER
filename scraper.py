import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# Make a request to the website
url = 'https://www.bobvila.com/articles/best-eco-friendly-products/'

# Send a GET request to the URL
response = requests.get(url)
# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# Find all image elements on the page
img_elements = soup.find_all('img')
save_directory = 'C:\\Users\myroslav\Desktop\CODING\SCRAPER\scraperImages'

# Save the images
for img in img_elements:
    image_url = img['src']
    if not image_url or image_url.startswith('data:'):
        continue
    filename = os.path.join(save_directory, image_url.split('/')[-1])
    # Download and save the image
    try:
        photo = urllib.request.urlopen(image_url).read()
        f = open(filename, "wb")
        f.write(photo)
        print(f'Saved: {filename}')
    except Exception as e:
        print(f'Error saving {image_url}: {e}')

f.close()        