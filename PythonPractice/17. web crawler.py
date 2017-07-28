'''Use the BeautifulSoup and requests Python packages to print out a list of all the
article titles on the New York Times homepage.'''


from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
headings = soup.findAll("h2", {"class": "story-heading"})

for heading in headings:
    if heading.findAll("a"):
        # .strip() removes leading/trailing whitespace
        print(heading.a.text.strip())
    else:
        print(heading.text)