from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.airbnb.com/s/Beirut/homes"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
lists = soup.findAll('div', attrs={"class": "c4mnd7m"})

with open('BeirutRentals.csv', 'w', encoding='utf8', newline='') as f:
    theWriter = writer(f)
    header = ['Title', 'NO.Beds', 'Price', 'Rating']
    theWriter.writerow(header)

    for list in lists:

        title = list.find('span', attrs={"class": "t6mzqp7"}).text.replace('★', ' ')
        nbOfBeds = list.find('span', attrs={"class": "dir dir-ltr"}).text
        price = list.find('span', attrs={"class": "a8jt5op"}).text
        rating = list.find('span', attrs={"class": "t5eq1io"}).text

        info = [title, nbOfBeds, price, rating]
        theWriter.writerow(info)


