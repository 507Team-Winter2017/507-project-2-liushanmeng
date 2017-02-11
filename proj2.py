#proj2.py
import requests
from bs4 import BeautifulSoup
# python3 proj2.py
#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
baseurl = 'http://www.nytimes.com'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all(class_="story-heading")[:10]:
	if story_heading.a:
		print(story_heading.a.text.replace("\n", " ").strip())
	else:
		print(story_heading.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
baseurl = 'https://www.michigandaily.com/'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")

pane = soup.find_all(class_="pane-mostread")[0]
for li in pane.find_all('li'):
	print (li.text.strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
baseurl = 'http://newmantaylor.com/gallery.html'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")

for image in soup.find_all('img'):
	if image.has_attr('alt'):
		print (image['alt'])
	else:
		print ("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
base = "https://www.si.umich.edu"#/node/9942"
baseurl = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
i = 1
while True:
	r = requests.get(baseurl)
	soup = BeautifulSoup(r.text, "html.parser")

	for div in soup.find_all(class_ = "field-name-contact-details"):
		baseurl = base + div.a["href"]
		r = requests.get(baseurl)
		soup_div = BeautifulSoup(r.text, "html.parser")
		
		div_email = soup_div.find_all(class_ = "field-name-field-person-email")[0]
		print ('{} {}'.format(i, div_email.a.text))
		i += 1
	pager_next = soup.find_all(class_="pager-next")[0]
	if pager_next.a:
		baseurl = base + pager_next.a["href"]
	else:
		break