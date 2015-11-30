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
        self.message = None


    def choose_receiver(self):
        flag = True
        while flag == True:
            self.receiver = raw_input("Pick recipient: ")
            if self.receiver == "print":
                self.display_addresses()
            else:
                for name, address in self.addresses.items():
                    if self.receiver == name:
                        self.address = address

                flag = False

        return self.address


    def get_message(self):
        self.message = raw_input("Enter message:")
        return self.append_header()

    def append_header(self):
        return self.version + self.sender + self.receiver + "\r\n" +  "\n" + self.message + "\n\n"


    def display_addresses(self):
        for name, address in self.addresses.items():
            print name, "-->", address


    def send_again(self, prompt):
        response = 'n'
        while response not in ("Y","N"):
            response = raw_input(prompt)
            response = response.upper()

        return response == "Y"


    def run_client(self):
        again = True
        while again:
            self.choose_receiver()
            self.get_message()
            print self.message




if __name__ == "__main__":
    client = TauClientInterface()
    client.run_client()
