from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")


anchor_tags = soup.find_all(name="span", class_="titleline")

articles = []
for tag in anchor_tags:
    score_tag = tag.find_next("span", class_="score")  # Find associated score
    upvotes = int(score_tag.get_text().split()[0]) if score_tag else 0
    articles.append({
        "title": tag.get_text(),
        "link": tag.a.get("href"),
        "upvotes": upvotes
    })

for article in articles:
    print(f"Title: {article['title']}, Upvotes: {article['upvotes']}, Link: {article['link']}")

# Find the most popular article
most_popular = max(articles, key=lambda x: x['upvotes'])

print("\nMost Popular Article:")
print(f"Title: {most_popular['title']}")
print(f"Link: {most_popular['link']}")
print(f"Upvotes: {most_popular['upvotes']}")
