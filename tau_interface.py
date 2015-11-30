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
    def __init__(self):
        self.address_book = json.load(open("tau_table.json"))
        self.addresses = self.address_book["Address_Book"]
        self.version = "Version: 0.2\r\n"
        self.sender = "chupacabra\r\n"
        self.receiver = None
        self.address = None
    #def pick_user(self):
        # pick_receiver = input("Enter a name to send message to: ")

    def main(self):
        self.choose_receiver()
        message = self.get_message()



    def choose_receiver(self):
        self.receiver = input("Pick recipent: ")
        for name in self.addresses:
            if self.receiver == name:
                self.address = self.addresses[name]


    def get_message(self):
        message = input("Enter message: ")
        return self.version + self.sender + self.reciever + "\r\n" + message

    def display_addresses(self):
        for name,address in self.addresses.items():
            print name, "-->", address

if __name__ == "__main__":
    client = TauClientInterface()
    client.main()
