from bs4 import BeautifulSoup

html_file = open("jJ4fRq-UA_PCC_XML.html").read()
soup = BeautifulSoup(html_file, "html.parser")

all_ps = soup.find_all("p", class_='s3')
for p in all_ps:
    this_text = p.text
    print(this_text.split(":"))

all_hs = soup.find_all("h2")
for h2 in all_hs:
    this_text = h2.text
    print(this_text.split("."))
