from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.findAll(class_="titleline")

# for article in articles:
#     print(article.contents[0].getText())
#     print(article.contents[0].get("href"))

# article_name = articles.contents[0].getText()
# article_link = articles.contents[0].get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

all_article_names = [article.contents[0].getText() for article in articles]
all_article_links = [article.contents[0].get("href") for article in articles]
all_article_upvotes = [int(upvote.text.split(' ')[0]) for upvote in soup.find_all(name="span", class_="score")]

# for i in range(len(articles)):  # print name, link and upvote of every article
#     print(f"{i}.{all_article_names[i]}")
#     print(all_article_links[i])
#     print(all_article_upvotes[i])
#     print("------")

highest_upvote_article_index = all_article_upvotes.index(max(all_article_upvotes))
print(all_article_names[highest_upvote_article_index + 1])
print(all_article_links[highest_upvote_article_index + 1])
print(all_article_upvotes[highest_upvote_article_index])

