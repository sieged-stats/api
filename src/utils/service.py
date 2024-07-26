import os

from dotenv import load_dotenv
from siegeapi import Auth

load_dotenv()

auth = Auth(os.getenv("UBISOFT_MAIL"), os.getenv("UBISOFT_PASSWORD"), cachetime=0)
