import time
from dotenv import load_dotenv, find_dotenv
from classes.Refresher import Refresher
from classes.repository.HeadHunterRepository import HeadHunterRepository

load_dotenv(find_dotenv())

if __name__ == "__main__":
    while True:
        print("Will start server")
        client = Refresher()
        client.execute()
        time.sleep(60*5)
