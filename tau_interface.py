# This will be the interface for the system
import json



def choice_display():
	choice = None
	while choice not in range(1,4):
		print( """
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
