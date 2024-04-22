from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

title_string = soup.title.string
# print(title_string) -> prints the value of title tag in html doc

all_anchor_tags = soup.findAll(name="a")  # name="x", x - can be any html tag
all_h3_tags = soup.findAll(name="h3")  # name="x", x - can be any html tag
# print(all_h3_tags) -> prints all h3 tags

# for h3_tag in all_h3_tags:
#     print(h3_tag.getText())  # print strings in all h3 tags

# for tag in all_anchor_tags:
#     print(tag.get("href"))  # tag.get("X"), where X - any attribute of a html tag

heading = soup.find(id="name")
# print(heading.name)  #

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())  # gets text

company_url = soup.select_one(selector="p a")  # gets the element, specify containers that your elements are in
print(company_url)

select_by_id = soup.select_one(selector="#name")
print(select_by_id)

select_by_class = soup.select(".heading")
print(select_by_class)