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
        self.client = None
        self.address_book = json.load(open("tau_table.json"))
        self.addresses = self.address_book["Address_Book"]
        self.version = "Version: 0.2\r\n"
        self.sender = "chupacabra\r\n"
        self.receiver = None
        self.address = None
        self.message = None


    def choose_receiver(self):
        while True:
            self.receiver = raw_input("Pick recipient: ")
            if self.receiver == "print":
                self.display_addresses()
            else:
                for name, address in self.addresses.items():
                    if self.receiver == name:
                        self.address = address
                break

        return self.address


    def get_message(self):
        while True:
            self.message = raw_input("Enter message:")
            if self.message == "exit":
                self.client.close_client()
            else:
                self.append_header()
                break


    def append_header(self):
        self.message = self.version + self.sender + self.receiver + "\r\n" +  "\n" + self.message + "\n\n"


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
        flag1 = True
        #flag2 = True
        while flag1:
            self.client = TauClient()
            self.choose_receiver()
            #while flag2:
            self.get_message()
            if self.message == "exit":
                flag2 = False
            else:
                self.client.connect_client(self.address, self.message)
            print self.message
            #flag2 = self.send_again("Send to "+ self.receiver + " again? ")
            flag1 = self.send_again("Send another message? ")
            #if flag1:
                #flag2 = True



if __name__ == "__main__":
    client = TauClientInterface()
    client.run_client()
