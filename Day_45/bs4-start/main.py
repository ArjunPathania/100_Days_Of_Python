from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

anchor_tags = soup.find_all(name="a")
print(anchor_tags)
for tag in anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))


heading = soup.find(name="h1",id="name")
print(heading)
section_heading = soup.find(name="h3",class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)