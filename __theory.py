# I just copied this table generator from a chinese programmer on GitHub. #
# and I'm still in progress of finding her bc I don't remember her name. #
ASC_A = ord("a")
TABLE_WIDTH = 26
ciphered = ""
def init_table():
	return [[chr((col + row) % TABLE_WIDTH + ASC_A) for col in range(TABLE_WIDTH)] for row in range(TABLE_WIDTH)]
# ^btw thanks for this vigenere square table #