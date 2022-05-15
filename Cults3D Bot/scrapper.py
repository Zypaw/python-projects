import requests
from bs4 import BeautifulSoup

def scrapping(url):
    r = requests.get(url) #get the request page
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser") #get the soup parser
        image = soup.find('img', {'class':'painting-image'}) #get the image url
        if image["src"].endswith(".gif"):
            for i in range(len(image["src"])):
                if image["src"][-6-i:-1-i] == "https":
                    image["src"] = image["src"][-6-i:-1]+"f"
                    break
        elif image["src"].endswith(".png"):
            for i in range(len(image["src"])):
                if image["src"][-6-i:-1-i] == "https":
                    image["src"] = image["src"][-6-i:-1]+"g"
                    break
        price = soup.find('span', {'class':'btn--breathing btn-group-end btn-third'})
        name = soup.find('h1', {'class':'t0'})
        if url[20:22] == "fr":
            download = soup.find('span', {'data-counter-text-singular':'téléchargement'})
        elif url[20:22] == "en":
            download = soup.find('span', {'data-counter-text-singular':'download'})
        return {
            "image_url" : str(image["src"]),
            "url" : url,
            "price" : str(price.text.strip()),
            "name" : str(name.text.strip()),
            "download" : int(download["data-counter-value"])
        }
    else :
        return { 
            "status" : "error",
            "code" : r.status_code
        }
