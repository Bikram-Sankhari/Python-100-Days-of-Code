from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
website = response.text

soup = BeautifulSoup(website, "html.parser")
movies = [tag.getText() for tag in soup.find_all(name="h3", class_="title")]

movies.reverse()

with open("Movies.text", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie)
        file.write("\n")
