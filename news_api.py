import requests

url = "https://newsdata.io/api/1/latest? \
  apikey=pub_0f46a3e35d664a1d84f729d600cba41e \
  &q=IDBI BANK \
  &country=in\
  &language=hi,en"

request = requests.get(url)
content = request.text

print(content)
