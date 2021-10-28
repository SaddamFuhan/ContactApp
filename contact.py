import os

class Contact:

	def __init__(self, App):
		self.settings = App.settings
		# self.contact_list = self.settings.load_data_contact()

	def search_contact(self, name):
		contact = self.settings.find_data_contact_by_name(name)
		if contact:
			print("Contact found")
			print(f"Name \t:{contact.nam}\tPhone \t:{contact.phone}")
		else:
			print("Not found")
		return contact


	def delete_contact(self):
		os.system("clear")
		print("\nDelete Contact")
		name = input("Name\t:")
		contact = self.search_contact(name)
		if contact:
			confirm = input("Are you sure to delete this contact ? (y/n) ")
			if confirm.lower() == 'y':
				self.settings.delete_data_contact(contact.nam)
				print("Contact delete.")
			else:
				print("Canceled.")
		input("Press ENTER to Main Menu")


	def find_contact(self):
		os.system("clear")
		print("\nFind Contact")
		name = input("Name\t:")
		contact = self.search_contact(name)

		input("Press ENTER to Main Menu")

	def add_contact(self):
		os.system("clear")
		print("\nAdd New Contact")
		name = input("Name\t:")
		phone = input("Phone\t:")
		confirm = input("Are you sure to save this contact ? (y/n) ")
		if confirm.lower() == 'y':
			self.settings.input_new_contact(name, phone)
			print("Contact Saved")
		else:
			print("Canceled")
		input("Press ENTER to Main Menu")

	def view_contacts(self):
		os.system("clear") #windows cls
		print("\nView All Contacts")
		contacts = self.settings.load_data_contact()
		if len(contacts) == 0:
			print("No contacts")
		else:
			for contact in contacts:
				print(contact.nam , contact.phone)

		input("Press ENTER to Main Menu")