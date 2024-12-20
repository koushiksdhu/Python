from bs4 import BeautifulSoup
import lxml


with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
# print(soup.h1.text)
# print(soup.h2.text)
# print(soup)
# print(soup.prettify())
# print(soup.title.text)
# print(soup.a)
# print(soup.a.text)


# FIND_ALL:
# we can find all the elements by passing the tag name.
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# Fetching text from all_anchor_tags using list comprehension:
# all_anchor_tags = [each.getText() for each in all_anchor_tags]
# print(all_anchor_tags)

# all_anchor_tags = [each.get("href") for each in all_anchor_tags]
# print(all_anchor_tags)

# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.text)

# heading = soup.find_all(name="h1", class_="heading")
# print(heading)
# heading = [i.getText() for i in heading]
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
# print(section_heading.name)
# print(section_heading.get("class"))

# all_urls = soup.select(selector="p a")
# print(all_urls)
# all_urls = [i.getText() for i in all_urls]
# print(all_urls)

# intixta_url = soup.select_one(selector="p a")
# print(intixta_url.text)

# Selecting ID:
# print(soup.select_one(selector="#name"))
# # print(soup.select_one("#name")) -> both syntax does the same thing.
# print(soup.select_one(selector="#name").text)

# Selecting CLASS:
# print(soup.select_one(".heading"))
# print(soup.select_one(".heading").text)
