import requests
from bs4 import BeautifulSoup
 
# scraping a wikipedia article
url_link = 'https://www.theoi.com/Text/LucianDialoguesGods1.html'

def save_book_as_md(url, name):
    request = requests.get(url)
    Soup = BeautifulSoup(request.text)
    heading_tags = ["h2", "h3", "p"]
    with open(str(name)+".md", 'w') as f:
        for tags in Soup.find_all(heading_tags):
            if tags.name == "h2":
                f.write("# " + tags.text.strip() + '\n')
            elif tags.name == "h3":
                f.write("## " + tags.text.strip() + '\n')
            elif tags.name == "p":
                f.write(tags.text.strip() + '\n')
            if tags.text.strip() == "THE END":
                break

save_book_as_md(url_link, "Lucian Dialogues of Gods")