from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-murder-mystery-movies"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movies_list = [movie.getText().split(" ", 1)[1]
               for movie in soup.select("h2 strong")]

with open("Movie Scrapping/Movies.txt", mode="w") as mov:
    for i in range(len(movies_list)):
        mov.write(str(i+1) + "." + movies_list[i] + "\n")

print(movies_list)
