import requests
from bs4 import BeautifulSoup as bs

#this will get the
github_user = input('Input Github User: ')

#this url is the page you want to send a request to
url = 'https://github.com/'+github_user

#this will send the request to the url the user inputs
r = requests.get(url)

#using r.content will give you everything on the url page
soup = bs(r.content, 'html.parser')

#using soup.find means the with the html file, we have to find the specific tag, class,attribute
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)

