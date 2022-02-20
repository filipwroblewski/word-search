""" Finding words in word search vertically and horizontally """

class Finder(object):
	"""Finder words in word search"""
	def __init__(self, arr, words):
		self.arr = arr
		self.words = words
		self.arr_words = words.split()
		self.arr_asnwers = []


	# Left to Right in Row Finding (LRRF)
	def lrrf(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr_words)):
				if self.arr_words[j] in self.arr[i]:
					# start = self.arr[i].find(self.arr_words[j])
					# end = self.arr[i].find(self.arr_words[j])+len(self.arr_words[j])
					self.arr_asnwers.append(self.arr_words[j])
		return self.arr_asnwers


	# Right to Left in Row Finding (RLRF)
	def rlrf(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr_words)):
				if self.arr_words[j][::-1] in self.arr[i]:
					# start = self.arr[i].find(self.arr_words[j])
					# end = self.arr[i].find(self.arr_words[j])+len(self.arr_words[j])
					self.arr_asnwers.append(self.arr_words[j][::-1])
		return self.arr_asnwers


	# Up to Down in Column Finding (UDCF)
	def udcf(self):
		for i in range(len(self.arr[0])):
			column = ''
			for j in range(len(self.arr)):
				column += self.arr[j][i]
			
			for h in range(len(self.arr_words)):
				if self.arr_words[h] in column:
					start = column.find(self.arr_words[h])
					end = column.find(self.arr_words[h])+len(self.arr_words[h])
					# return self.arr_words[h]
					# print(arr_words[h], column[start:end])
					self.arr_asnwers.append(self.arr_words[h])
		return self.arr_asnwers


	# Down to Up in Column Finding (DUCF)
	def ducf(self):
		for i in range(len(self.arr[0])):
			column = ''
			for j in range(len(self.arr)):
				column += self.arr[j][i]
			
			for h in range(len(self.arr_words)):
				if self.arr_words[h][::-1] in column:
					start = column.find(self.arr_words[h])
					end = column.find(self.arr_words[h])+len(self.arr_words[h])
					# print(self.arr_words[h], column[start:end])
					# return self.arr_words[h]
					self.arr_asnwers.append(self.arr_words[h][::-1])
		return self.arr_asnwers
