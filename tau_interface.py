"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin:
Rachael Johnson:
Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/
"""

def choice_display():
    choice = None
    while choice not in range(1, 4):
        print("""
                TauNet Messaging System v.1

                1. Receive Messages
                2. Send Message
                3. Exit Program
                """)

        try:
            choice = int(input("Make selection: "))
        except ValueError:
            print("Not a valid choice")


def main():
    choice = choice_display()


if __name__ == "__main__":
    main()
