from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web"
                            "/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")

all_title = soup.findAll("h3")

movie_list = [title.getText() for title in all_title[::-1]]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.writelines(f"{movie}\n")
