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
        # def pick_user(self):
        # pick_receiver = input("Enter a name to send message to: ")

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

    def append_header(self, message):
        return self.version, self.sender,self.receiver + "\r\n", "\n", message

    def display_addresses(self):
        for name, address in self.addresses.items():
            print name, "-->", address


def main():
    prep_client = TauClientInterface()
    client = TauClient()


    flag = True
    while flag:
        host = None
        host = prep_client.choose_receiver()
        print host
        message = get_message()
        if message == "exit":
            flag = False
            client.close_client()
            break

        else:
            message = prep_client.append_header(message)
            client.connect_client(host, message)




def get_message():
    return raw_input("Enter message:")


if __name__ == "__main__":
    main()
