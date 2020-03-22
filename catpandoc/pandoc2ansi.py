"""Convert a pandoc string to ansi
"""
import urllib
import os
import catimage
import art

import pygments
from pygments.formatters import Terminal256Formatter
from pygments.lexers import get_lexer_by_name

from catpandoc import processpandoc
from catpandoc.pandoc2plain import Pandoc2Plain


class Pandoc2Ansi(Pandoc2Plain):
	"""Convert a pandoc string to ansi. Inherits from Pandoc2Plain (no need
	for identical methods - down with code duplication...)
	"""
	def __init__(self, width=80, padding=0, baseColour=(4, 0, 4)):
		self.content = []
		self.width = width - padding * 2
		self.padding = padding
		self.baseColour = baseColour
		# Constants
		self.FG = "\033[38;5;"
		self.BG = "\033[48;5;"
		self.CLR_FG = "\033[39m"
		self.CLR_BG = "\033[49m"
		self.CLR = "\033[0m"


	#########################################
	# UTIL
	#########################################

	def catImage(self, content):
		'''catImage '''
		self.print(self.CLR)
		try:
			if content.startswith("http"):
				urllib.request.urlretrieve(content, "dowloadedImage")
				content = "dowloadedImage"
			try:
				self.print(catimage.generateHDColour(os.getcwd() + os.sep + content,
				self.width))
			except FileNotFoundError:
				self.print(content)
		except urllib.error.HTTPError:
			self.print(content)
		self.print(self.CLR, end="")


	#########################################
	# BLOCK
	#########################################

	def header(self, content):
		'''Process a header '''
		self.print("\n", end="")
		concatContent = ""
		headColour = [0,
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (1, 1, 1))),
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (1, 0, 0))),
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, 0))),
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, -1))),
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1))),
		self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2)))]
		if content[0] > 3:
			self.print(self.FG + headColour[content[0]], end="")
			for part in content[-1]:
				processpandoc.processInline(part, self)
			self.print(self.CLR, end="")
		else:
			concatContent = "".join([processpandoc.toPlaintext(part) for part in content[-1]])
			if any(char in concatContent for char in ["q", "y", "p", "g", "j"]):
				limit = 1
			else:
				limit = 2
			if content[0] == 1:
				if len(concatContent) > self.width / 7:
					concatContent = concatContent[:int(self.width / 7)]
				self.print(self.FG + headColour[content[0]] +
				"\n".join(art.text2art(concatContent, "swan").split("\n")[2:-limit-1]))
				self.print("▀"*self.width + self.CLR)
			if content[0] == 2:
				if len(concatContent) > self.width / 5:
					concatContent = concatContent[:int(self.width / 5)]
				self.print(self.FG + headColour[content[0]] +
				"\n".join(art.text2art(concatContent, "thin").split("\n")[1:-limit]))
				self.print("━"*self.width + self.CLR)
			if content[0] == 3:
				if len(concatContent) > self.width / 3:
					concatContent = concatContent[:int(self.width / 3)]
				self.print(self.FG + headColour[content[0]] +
				"\n".join(art.text2art(concatContent, "cygnet").split("\n")[1:-limit]))
				self.print("─"*self.width + self.CLR)

	def codeBlock(self, content):
		'''Process a code block  '''
		codeColour = self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1)))
		self.print(self.FG + codeColour + "\n │ " + self.CLR_FG, end="")
		try:
			self.print(self.FG + codeColour + " │ ".join([self.CLR_FG +
			pygments.highlight(line, get_lexer_by_name(content[0][1][0]), Terminal256Formatter()) +
			self.CLR for line in content[1].split("\n")]))
		except:
			self.print(self.FG + codeColour + "\n │ ".join(content[1].split("\n")) + self.CLR_FG)

	def definitionList(self, content):
		'''Process a definition list '''
		for definition in content:
			#for definition in definitionBlock:
			self.newline()
			self.print(self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end="")
			for part in definition[0]:
				processpandoc.processInline(part, self)
			self.print("\t:"+ self.CLR_FG + ":\t", end="")
			for part in definition[1]:
				for partB in part:
					processpandoc.processBlock(partB, self)


	def orderedList(self, content):
		'''Process an ordered list '''
		self.print(self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end="")
		for index, bullet in enumerate(content[1]):
			self.print("\n", index+1, end=". ")
			for point in bullet:
				if point["t"] in ["BulletList"]:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)
		self.print(self.CLR_FG, end="")

	def bulletList(self, content):
		'''Process a bulleted list '''
		self.print(self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end="")
		for bullet in content:
			for point in bullet:
				if point["t"] not in ["BulletList"]:
					self.print("\n- ", end="")
				else:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)
		self.print(self.CLR_FG, end="")

	# Table

	def blockQuote(self, content):
		'''Process a block quote '''
		print("\n" + self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-2, -2, -2))) +
		" ┃ ", end="")
		print("\n ┃ ".join([processpandoc.toPlaintext(block).split("\n") for block in content][0]) +
		self.CLR_FG)


	#########################################
	# INLINE
	#########################################

	# Space

	def emph(self, content):
		'''Process emphasized text '''
		for newInline in content:
			self.print("\033[3m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[23m", end="")

	def strong(self, content):
		'''Process strong (bold) text '''
		for newInline in content:
			self.print("\033[1m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[21m", end="")

	def strikeout(self, content):
		'''Process strikeout (crossed out) text '''
		for newInline in content:
			self.print("\033[9m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[29m", end="")

	# Superscript

	# Subscript

	# SmallCaps

	# Quoted

	def code(self, content):
		'''Process code '''
		self.print(self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1))) +
		" │" + content[1], end="│ " + self.CLR_FG)

	# Math

	# Note

	# Span

	# Image

	# Link

	def hr(self):
		'''Process a hr '''
		self.print(self.FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, 0))) +
		"─"*self.width + self.CLR_FG)


	def ansiFromAnsiRgb(self, colour):
		'''Generates ansi based on reduced rgb ie in range 0-5 '''
		r, g, b = (colour)
		return str(int(16 + min(max(r, 0), 5) * 36 + min(max(g, 0), 5) * 6 + min(max(b, 0), 5))) + "m"

	def varBaseC(self, base, modify):
		'''Generates a colour based on the theme colour '''
		newC = []
		for index in range(3):
			newC.append(base[index] + modify[index])
		return newC
