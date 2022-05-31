import requests
url_books = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

http_rsp = requests.get(url_books)
print(http_rsp.json)

for book in http_rsp.json():
    print(f"Book name:  {book['name']}")

