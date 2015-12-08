#!/usr/bin/python
"""

 Copyright (C) 2015 RJ Russell
 Created with the collaborative assistance of::
 Jacob Martin, Rachael Johnson, Andrew Wood:

 References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
             Python Docs:........................https://www.python.org/

 tau_interface.py

 This file is responsible for all the user interactions with the client side.
 It prompts the user for a recipient and a message. There are built in flags to
 assist the user if needed. The flags list the address book or display the help message.
 When sending a message the header is appended to the message in the correct format.
 The interface loops until the user enters "exit" for a recipient or for a message.
"""
import json
import operator
import os
from code_files.tau_client import TauClient


class TauClientInterface:
    def __init__(self):
        """ Initializes all variables needed, including reading in the address book from a json file """
        self.client = None
        self.address_book = json.load(open("code_files/address_book.json"))
        self.addresses = self.address_book["Address_Book"]
        self.version = "version: 0.2\r\n"
        self.sender = "from: chupacabra\r\n"
        self.receiver = None
        self.address = None
        self.message = None
        self.time_stamp = None

    def choose_receiver(self):
        """
        Prompts user to pick a recipient. If a flag is entered
        displays the information associated with that flag. If an invalid
        recipient is entered, displays message and loops to the prompt.
        If "exit" is entered, exits program.
        """
        flag = True
        while flag:
            self.receiver = raw_input("Pick recipient: ")
            if self.receiver in ("-address", "-a"):
                self.display_addresses()
            elif self.receiver in ("-help", "-h"):
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
                    print "(-help(-h) for help menu, -address(-a) to display addresses.\n\n"

    def get_message(self):
        """ Prompts and reads in message to send from user. If "exit" is entered, exits program. """
        self.message = raw_input("Enter message: ")
        if self.message == "exit":
            self.exit_program()

    def append_header(self):
        """ Appends header information to message """
        self.message = self.version + self.sender + "to: " + self.receiver + "\r\n" + "\r\n" + self.message

    def display_addresses(self):
        """ Displays address book in sorted order by username """
        # Makes copy of address dictionary so the original is not affected.
        addresses = self.addresses
        addresses = sorted(addresses.items(), key=operator.itemgetter(0))
        for name, address in addresses:
            print name, "-->", address
        print "\n\n"

    @staticmethod
    def display_help():
        """ Displays help message """
        print """
        -address (-a):  display address book
           -help (-h):  displays the help message

        'clear': clears the client screen (only on recipient prompt)
         'exit': exits program
          ('exit' can be entered on recipient/message prompt to exit program.)

        Choose a person to send a message to by entering in the user name of the
        intended recipient.

        """

    @staticmethod
    def clear():
        """ Clears the screen """
        os.system('clear')

    def exit_program(self):
        print ("Exiting Client..")
        self.client.close_client()
        exit(-1)

    def run_client(self):
        """
        Responsible for the logic for this part of the program.
        Creates necessary objects, chooses reciever, gets message, appends header
        and sends message. If message is successful displays sent message.
        Continues to loop until user exits the program.
        """
        flag1 = True
        while flag1:
            self.client = TauClient()
            self.choose_receiver()

            self.get_message()
            if self.message == "exit":
                self.exit_program()
            else:
                self.append_header()
                success = self.client.connect_client(self.address, self.message)

                if not success == -1:
                    print self.message

if __name__ == "__main__":
    client = TauClientInterface()
    client.run_client()
