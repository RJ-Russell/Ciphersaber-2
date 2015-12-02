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
        self.version = "version: 0.2\r\n"
        self.sender = "from: chupacabra\r\n"
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
                else:
                    print "Recipient entered was not found."
                    print "\nPlease try again."
                    print "(--help(-h) for help menu, --list(-l) to display addresses.\n\n"

    def get_message(self):
        while True:
            self.message = raw_input("Enter message: ")
            if self.message == "exit":
                self.exit_program()
            else:
                self.append_header()
                break


    def append_header(self):
        self.message = self.version + self.sender + "to: " + self.receiver + "\r\n" + self.message + "\n\n"


    def display_addresses(self):
        for name, address in self.addresses.items():
            print name, "-->", address
        print "\n\n"

    def display_help(self):
        print """
        --list (-l): prints the address book
        --help (-h): displays the help message

        'clear': clears the client screen (only on recipient prompt)
        'exit': exits program
          ('exit' can be entered on recipient/message prompt to exit program.)

        Choose a person to send a message to by entering in the user name of the
        intended recipient.

        """


    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def exit_program(self):
        print ("Exiting Client..")
        self.client.close_client()
        exit(-1)

    def run_client(self):
        flag1 = True
        while flag1:
            self.client = TauClient()
            self.choose_receiver()

            self.get_message()
            if self.message == "exit":
                self.exit_program()
            else:
                success = self.client.connect_client(self.address, self.message)

                if not success == -1:
                    print self.message




if __name__ == "__main__":
    client = TauClientInterface()
    client.run_client()
