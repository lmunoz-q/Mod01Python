import sys


class GotCharacter:
	def __int__(self, first_name, is_alive=True):
		try:
			if not isinstance(first_name, str) or first_name == "":
				raise TypeError("error, 'first_name' must be a <non empty string>")
			self.first_name = first_name
		except TypeError as te:
			sys.exit(te)
