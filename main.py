
from settings import Settings
from user import User
from interface import Interface
from contact import Contact


class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.contact = Contact(self)
		self.interface = Interface()
		self.user = User()

	def check_input(self):
		current_input = self.user.current_input.lower()
		if current_input == 'q':
			self.settings.active = False
		elif current_input == '1':
			self.contact.view_contacts()
		elif current_input == '2':
			self.contact.add_contact()
		elif current_input == '3':
			self.contact.find_contact()
		elif current_input == '4':
			self.contact.delete_contact()

	def run(self):
		while self.settings.active:
			self.interface.main_menu()
			self.user.input_prompt()
			self.check_input()

if __name__ == '__main__':
	my_contact_app = ContactApp()
	my_contact_app.run()