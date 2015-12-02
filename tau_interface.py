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
import os
from tau_client import TauClient


class TauClientInterface:
    def __init__(self):
        self.client = None
        self.address_book = json.load(open("tau_table.json"))
        self.addresses = self.address_book["Address_Book"]
        self.version = "Version: 0.2\r\n"
        self.sender = "From: chupacabra\r\n"
        self.receiver = None
        self.address = None
        self.message = None


    def choose_receiver(self):
        flag = True
        while flag:
            self.receiver = raw_input("Pick recipient: ")
            if self.receiver in ("--list", "-l"):
                self.display_addresses()
            elif self.receiver in ("--help", "-h"):
                self.display_help()
            elif self.receiver == 'clear':
                self.clear()
            elif self.receiver == 'exit':
                self.exit_program()
            else:
                for name, address in self.addresses.items():
                    if self.receiver == name:
                        self.address = address
                        print self.address
                        flag = False
                        break


    def get_message(self):
        while True:
            self.message = raw_input("Enter message: ")
            if self.message == "exit":
                self.client.close_client()
            else:
                self.append_header()
                break


    def append_header(self):
        self.message = self.version + self.sender + "To: " + self.receiver + "\r\n" +  "\n\nMessage: " + self.message + "\n\n"


    def display_addresses(self):
        for name, address in self.addresses.items():
            print name, "-->", address

    def display_help(self):
        print """
        --list (-l): prints the address book
        --help (-h): displays the help message

        'clear': clears the client screen
        'exit': exits program

        Choose a person to send a message to by entering in the user name of the
        intended recipient.

        """

    def send_again(self, prompt):
        response = 'n'
        while response not in ("Y","N"):
            response = raw_input(prompt)
            response = response.upper()

        return response == "Y"

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def exit_program(self):
        print ("Exiting Client..")
        exit(-1)

    def run_client(self):
        flag1 = True
        while flag1:
            self.client = TauClient()
            self.choose_receiver()

            self.get_message()
            if self.message == "exit":
                flag2 = False
            else:
                self.client.connect_client(self.address, self.message)
            print self.message
            flag1 = self.send_again("Send another message? ")


if __name__ == "__main__":
    client = TauClientInterface()
    client.run_client()
