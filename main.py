import requests
from send_email import send_email

topic = "tesla"
api_key = "85fb4dee7f844a8abbc7d177babd1f82"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-08-05&" \
      "sortBy=publishedAt&" \
      "apiKey=85fb4dee7f844a8abbc7d177babd1f82&" \
      "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    body = body + str(article["title"]) + "\n" \
           + str(article["description"]) + "\n" \
           + str(article["url"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
