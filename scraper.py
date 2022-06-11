import requests
from bs4 import BeautifulSoup

def scrape_article_text(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find("h1",class_="title-detail")
    text_elements = soup.findAll("p", class_="Normal")
    description_element = soup.find("p",class_="description")
    location_stamp = soup.find("span",class_="location-stamp")
    full_article = title_element.text
    if location_stamp != None : 
        full_article = full_article.replace(location_stamp.text, "", 1) 
        full_article += "\n" + location_stamp.text
        full_article += description_element.text.replace(location_stamp.text, ". ", 1)
    for element in text_elements:
        full_article += "\n" + element.text
    return full_article