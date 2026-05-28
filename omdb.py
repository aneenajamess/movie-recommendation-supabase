import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")

def get_movie(title):

    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    response = requests.get(url)# to get data from omdb server

    data = response.json()# the data sent by omdb is in json, .json() will convert it into dic

    return data