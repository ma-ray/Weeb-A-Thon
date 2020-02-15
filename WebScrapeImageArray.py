

import requests
from bs4 import BeautifulSoup
from requests import get
import os.path



def removeNewline(string):
    string = string.split('\n')
    s = ''
    for i in string:
        s += i.strip()
    return s


def profileLoad(user="EpicSteve2"):
    profileSoup = BeautifulSoup(get("https://myanimelist.net/profile/" + user).text, "html.parser")


def main():
    animeSoup = BeautifulSoup(get("https://myanimelist.net/anime/season").text, "html.parser")
    animeList = animeSoup.findAll('div', class_="seasonal-anime js-seasonal-anime")
    array=[]

    for anime in animeList:
        if (anime.find('div',class_="image").a.img.get('src') == None):
            image_url=anime.find('div',class_="image").a.img.get('data-src')
        else:
            image_url=anime.find('div', class_="image").a.img.get('src')
        array.append(image_url)



if __name__ == "__main__":
    main()