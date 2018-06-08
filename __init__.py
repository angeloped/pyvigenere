#!/usr/bin/env python
import sys
import __theory

"""
MIT License
The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. It is a form of polyalphabetic substitution.



Copyright (c) 2018 Bryan Angelo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
class pyvigenere:
	def __init__(self, __theory):
		self.theory = __theory.init_table()
		
	def cipher(self, data, key):
		if len(data) < len(key):
			key = key[:len(data)]
		
		key_clone = key
		key = ""
		
		for key_chr in key_clone:
			if key_chr.isalpha():
				key += key_chr
		
		key = key.lower()
		encode_str = ""
		tencstr = ""
		
		iiiii=1
		while bool(data):
			tencstr = data[:len(key)]
			data = data[len(key):]
			i = 0
			for cutted_data in tencstr:
				if cutted_data.isalpha():
					if tencstr[i].isupper():
						input_encode = cutted_data.lower()
						token = 1
					else:
						input_encode = cutted_data
						token = 0
					char_index = self.theory[0].index(input_encode)
					for a in self.theory:
						if a[0] == key[i]:
							if token == 1:
								encode_str += a[char_index].upper()
							else:
								encode_str += a[char_index]
				elif cutted_data.isdigit() or cutted_data == " ":
					encode_str += cutted_data
				else:
					encode_str += cutted_data
				i += 1
			tencstr = ""
			iiiii += 1
		return encode_str
	
	def decipher(self, data, key):
		if len(data) < len(key):
			key = key[:len(data)]
		
		key_clone = key
		key = ""
		for key_chr in key_clone:
			if key_chr.isalpha():
				key += key_chr
		
		key = key.lower()
		decode_str = ""
		tdecodestr = ""
		
		while bool(data):
			tdecodestr = data[:len(key)]
			data = data[len(key):]
			i = 0
			for cutted_data in tdecodestr:
				if cutted_data.isalpha():
					if cutted_data.isupper():
						input_decode = cutted_data.lower()
						token = 1
					else:
						input_decode = cutted_data
						token = 0
					for a in self.theory:
						if a[0] == key[i]:
							char_index = self.theory[0][a.index(input_decode)]
							if token == 1:
								decode_str += char_index.upper()
							else:
								decode_str += char_index
				elif cutted_data.isdigit() or cutted_data == " ":
					decode_str += cutted_data
				else:
					decode_str += cutted_data
				i += 1
			tdecodestr = ""
		return decode_str

def encode(data, key):
	"""
	encode(..., key)
	
	cipher the plain normal text.
	"""
	return pyvigenere(__theory).cipher(data, key)
def decode(data, key):
	"""
	decode(..., key)
	
	decipher the ciphered text.
	"""
	return pyvigenere(__theory).decipher(data, key)

if __name__ == "__main__":
	# perform demo testing
	if sys.version[0] >= "3":
		data = input("Enter data: ")
		key = input("Enter key: ")
	elif sys.version[0] <= "2":
		data = raw_input("Enter data: ")
		key = raw_input("Enter key: ")

	enc_dat = encode(data, key)
	dec_dat = decode(enc_dat, key)
	
	print("encode: {0}".format(enc_dat))
	print("decode: {0}".format(dec_dat))