from dotenv import load_dotenv, find_dotenv
from classes.Refresher import Refresher

load_dotenv(find_dotenv())

if __name__ == "__main__":
    print("Will start server")
    client = Refresher()
    client.execute()
