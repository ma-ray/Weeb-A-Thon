

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
    fileWrite = open("test.txt", "w")

    for anime in animeList:
        fileWrite.writelines((anime.find('div', class_="title").text.split('\n')[1]) + "\n")
        fileWrite.writelines(removeNewline(anime.find('div', class_="synopsis js-synopsis").text.strip()) + "\n")

        for genre in ((anime.find('div', class_="genres js-genre").find('div',class_="genres-inner js-genre-inner")).text.strip().split('\n\n')):
            fileWrite.write(genre + ",")
        fileWrite.write("\n")

        fileWrite.writelines((anime.find('div', class_="eps").text.split('\n\n')[0].strip()) + "\n")
        fileWrite.writelines((anime.find('div', class_="prodsrc").text.split('\n\n')[0].strip()) + "\n")
        fileWrite.writelines((anime.find('span', class_="source").text) + "\n")
        fileWrite.writelines((anime.find('div', class_="information").find('span', class_="member fl-r").text.strip()) + "\n")
        fileWrite.writelines((anime.find('span', class_="score").text.strip() + "\n\n"))
        if (anime.find('div',class_="image").a.img.get('src') == None):
            image_url=anime.find('div',class_="image").a.img.get('data-src')
        else:
            image_url=anime.find('div', class_="image").a.img.get('src')
        img_data = requests.get(image_url).content
        if('/'  not in ((anime.find('div', class_="title").text.split('\n')[1]))):
            with open( (anime.find('div', class_="title").text.split('\n')[1]) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        else:
            with open(( (anime.find('div', class_="title").text.split('\n')[1]) + '.jpg').replace('/','-'), 'wb') as handler:
                handler.write(img_data)

    fileWrite.close()
    print("Item has been written!")


if __name__ == "__main__":
    main()