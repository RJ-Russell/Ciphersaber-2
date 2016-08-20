# TauNet Messenger Software version 1.0
## Using TauNet Protocol Specification v. 0.2
### Copyright © 2015 RJ Russell
## General Software Information
This software was written using Python 2.7.

This software contains three major categories: Listening Server, Client Interface, and Address Book.

The Client Interface contains two files, one in which the user interacts with,
and one that is responsible for connecting to the message recipient’s address
and sending the message through a series of socket calls.
## Configuration
The TauNet system requires an internet connection.

**Port:** Can be set in tau_server.py and tau_client.py.

**Key scheduling:** 20 rounds (or set your own: rc4.py).

**Key:** password (or make your own: tau_server.py and tau_client.py)

**Address Book:** This application requires you to make your own JSON formatted address book.

    **Example**:

    {
       "Address_Book": {
         "username1": "username.ddns.net",
         "username2": "username2.com",
    }

This software has only been tested on Linux Debian based systems. Installing this on any other
platform is considered at your own risk and you assume full responsibility.
Installation and Running the Software

To install simply clone the Github repo.

This TauNet messenger software contains two independent scripts for the Client Interface and
Server.

## To run the TauNet messenger:
1. Server:
  * Open terminal.
  * From command line enter: ./tau_server.py

The server, once started is a simple listening program that displays the contents that is
sent to you.

In a separate terminal do the following:

2. Client:
  * Open terminal.
  * From command line enter: ./tau_interface.py
The client interface is responsible for reading in the address book from the JSON file and
prompting the user for the recipient and for the message. As stated earlier, the client
interface works in conjunction with the client.Built in Flags and Commands

The following flags and commands can be used in the tau_interface.

From the recipient prompt:
  * -address or –a: displays address book
  * -help or –h: displays help message
  * exit: exits tau_interface
  * clear: clears the tau_interface screen

From the message prompt:
  * exit: exits the tau_interface

## File Manifest
  * tau_interface.py
  * tau_server.py

### code_files
  * tau_client.py
  * rc4.py

### docs directory
  * SDD.pdf
  * SRS.pdf
  * STP.pdf

## License
This work is licensed under the "MIT License". Please see the file LICENSE in the source
distribution of this software for license terms.

## Bugs
This system currently runs as intended. Currently no known bugs.
