import requests
from send_email import send_email

url = "https://newsdata.io/api/1/latest? \
  apikey=pub_0f46a3e35d664a1d84f729d600cba41e \
  &q=IDBI BANK \
  &country=in\
  &language=hi,en"

#Made Request to the api here
request = requests.get(url)
#Got the dictionary of items here
content = request.json()

result = content['results']

news_string = ""

#Printed the title,image,description,published date here
for index,r in enumerate(result):
    news_string += f"News {index+1}" + '\n'
    news_string += r['title'] + '\n'
    news_string += r['description'] + '\n'
    news_string += r['image_url'] + '\n'
    news_string += r['pubDate'] + '\n'

news_string = news_string.encode('utf-8')
send_email(news_string)
