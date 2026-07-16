import requests
from send_email import send_email

topic = "IDBI BANK"
key = "pub_0f46a3e35d664a1d84f729d600cba41e"
language = "hi,en"

url = "https://newsdata.io/api/1/latest?" \
  f"apikey={key}" \
  f"&q={topic}" \
  "&country=in"\
  f"&language={language}"

#Made Request to the api here
request = requests.get(url)
#Got the dictionary of items here
content = request.json()

#We want 5 items from the list
result = content['results'][:5]

news_string = ""

#Printed the title,image,description,published date here
for index,r in enumerate(result):
    #Adding subject to the email
    news_string += "Subject: Today's news" + '\n'
    news_string += f"News {index+1}" + '\n'
    news_string += r['title'] + '\n'
    news_string += r['description'] + '\n'
    news_string += r['image_url'] + '\n'
    news_string += r['pubDate'] + '\n'

news_string = news_string.encode('utf-8')
send_email(news_string)
