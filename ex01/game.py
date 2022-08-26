import sys


class GotCharacter:
	def __int__(self, first_name, is_alive=True):
		try:
			if not isinstance(first_name, str) or first_name == "":
				raise TypeError("error, 'first_name' must be a <non empty string>")
			self.first_name = first_name
			self.is_alive = is_alive
		except TypeError as te:
			sys.exit(te)


class Stark(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(f"{self.house_words}")

	def die(self):
		self.is_alive = False

