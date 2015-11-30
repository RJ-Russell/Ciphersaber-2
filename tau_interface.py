"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin:
Rachael Johnson:
Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/
"""
import json
from tau_client import TauClient

class TauClientInterface:
    address_book = json.load(open("tau_table.json"))
    version = "Version: 0.2\r\n"
    sender = "chupacabra"
    receiver = None

    def pick_user(self):
        pick_receiver = input("Enter a name to send message to: ")
        


    def main():




if __name__ == "__main__":
    main()
