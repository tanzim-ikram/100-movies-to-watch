import requests
from bs4 import BeautifulSoup


# URL to scrap from
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

list_title = soup.title.string
movie_list_title = list_title.split("|")[0]

movie_titles = []

# Finding all the movies from the web page
all_movies = soup.find_all(name="h3", class_="title")

for movie in all_movies:
    title = movie.getText()
    movie_titles.append(title)

# Reversing the order of the movie lists
movies = movie_titles[::-1]

# Creating a file to store the movie lists
with open("movies.txt", encoding="utf8", mode="w") as file:
    file.write(f"{movie_list_title}\n")
    for movie in movies:
        file.write(f"{movie}\n")
