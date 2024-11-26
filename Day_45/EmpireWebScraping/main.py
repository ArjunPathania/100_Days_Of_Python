import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page,"html.parser")

movies = soup.find_all(name="h3" , class_='title')
movies_list = []
for movie in movies:
    movies_list.append(movie.get_text())

with open("movies.txt",mode="a") as file:
    for _ in range(1,101):
        file.write(movies_list[100 - _])
        file.write("\n")