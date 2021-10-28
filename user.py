class User:

	def __init__(self):
		self.current_input = None

	def input_prompt(self):
		self.current_input = input("Your Input : ")