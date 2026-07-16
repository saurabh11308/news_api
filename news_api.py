import requests

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

#Printed the title,image,description,published date here
for r in result:
    print(r['title'])
    print(r['description'])
    print(r['image_url'])
    print(r['pubDate'])