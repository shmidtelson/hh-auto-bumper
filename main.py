from dotenv import load_dotenv, find_dotenv
from classes.Refresher import Refresher

load_dotenv(find_dotenv())

client = Refresher()
client.handle()
