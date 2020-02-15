from bs4 import BeautifulSoup
from requests import get


class a:
    title=""
    synopsis=""
    genre=[]
    numOfEpisodes=""
    producer=""
    type=""
    numOfMembers=""
    score=""

    def __init__(self, title, syn, gen, ep, pro, tp, mem, sc):
        self.title=title
        self.synopsis=syn
        self.genre=gen
        self.numOfEpisodes=ep
        self.producer=pro
        self.type=tp
        self.numOfMembers=mem
        self.score=sc


def removeNewline(string):
    string=string.split('\n')
    s=''
    for i in string:
        s+=i.strip()
    return s


def profileLoad(user = "EpicSteve2"):
    profileSoup = BeautifulSoup(get("https://myanimelist.net/profile/" + user).text, "html.parser")


def main():
    animeSoup = BeautifulSoup( get("https://myanimelist.net/anime/season").text, "html.parser")
    animeList = animeSoup.findAll('div', class_="seasonal-anime js-seasonal-anime")
    animes=[]
    for anime in animeList:
        animes.append(a(
        (anime.find('div',class_="title").text.split('\n')[1]),#title
        removeNewline(anime.find('div',class_="synopsis js-synopsis").text.strip()),#syn
        ((anime.find('div', class_="genres js-genre").find('div',class_="genres-inner js-genre-inner")).text.strip().split('\n\n')),#gen
        (anime.find('div',class_="eps").text.split('\n\n')[0].strip()),#eps
        (anime.find('div', class_="prodsrc").text.split('\n\n')[0].strip()),  # producer
        (anime.find('span',class_="source").text) , # type
        (anime.find('div', class_="information").find('span', class_= "member fl-r").text.strip()) , # mem
        (anime.find('span', class_="score").text.strip())  # type
        ))
    
        
    fileWrite = open("test.txt", "w")
        
    for current in animes[:10]:
        fileWrite.writelines(current.title + "\n")
        fileWrite.writelines(current.synopsis + "\n")
        
        for genre in current.genre:
            fileWrite.write(genre + ",")
        fileWrite.write("\n")
        
        fileWrite.writelines(current.numOfEpisodes + "\n")
        fileWrite.writelines(current.producer + "\n")
        fileWrite.writelines(current.type + "\n")
        fileWrite.writelines(current.numOfMembers + "\n")
        fileWrite.writelines(current.score + "\n\n")
        
    fileWrite.close()
    print("Item has been written!")

if __name__ == "__main__":
    main()