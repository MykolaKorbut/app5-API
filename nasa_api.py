import requests
import streamlit as st

api_key = "wrw9t2xgPg4m03DgRBrK5SaoW9u8OVnVEG7W3C5A"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

title = content["title"]

image_url = content["url"]
request_image = requests.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(request_image.content)

explanation = content["explanation"]

#st.title("Mykola Korbut")
#st.image(image, width=400)

st.title(title)
st.image("image.jpg")
st.write(explanation)
