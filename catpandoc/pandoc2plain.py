"""Convert a pandoc string to plaintext
"""
from __future__ import annotations
from typing import Any

import urllib.request
import urllib.error
import os
import catimage
import art

from catpandoc import processpandoc, pandoc2xyz
from catpandoc.types import Alignment, Caption, Inline, Block, TableHead, TableBody

class Pandoc2Plain(pandoc2xyz.Pandoc2XYZ):
	"""Convert a pandoc string to plaintext
	"""
	def __init__(self, width: int=80, padding:int =0):
		self.content = []
		self.width = width - padding * 2
		self.padding = padding


	#########################################
	# UTIL
	#########################################

	def newline(self):
		'''newline '''
		self.print()

	def catImage(self, content: str):
		'''catImage '''
		try:
			if content.startswith("http"):
				urllib.request.urlretrieve(content, "dowloadedImage")
				content = "dowloadedImage"
			try:
				self.print(catimage.generateGreyscale(os.getcwd() + os.sep + content,
				self.width))
			except FileNotFoundError:
				self.print(content)
		except urllib.error.HTTPError:
			self.print(content)


	def print(self, *args: object, end: str="\n") -> None:
		'''Define a custom print method that has a very similar signature
		to the inbuilt print method '''
		self.content.append(" ".join([str(text) for text in args]) + end)

	def genOutput(self) -> str:
		'''Generate output '''
		lines = "".join(self.content).split("\n")
		out = []
		for line in lines:
			out.append(" " * self.padding + line)
		return "\n".join(out)

	#########################################
	# BLOCK
	#########################################

	def header(self, content: tuple[int, Any, list[Inline]]):
		'''Process a header '''
		self.print("\n", end="")
		concatContent = ""
		if content[0] > 3:
			for part in content[2]:
				processpandoc.processInline(part, self)
		else:
			concatContent = "".join([processpandoc.toPlaintext(part) for part in content[2]])
			if any(char in concatContent for char in ["q", "y", "p", "g", "j"]):
				limit = 1
			else:
				limit = 2
			if content[0] == 1:
				if len(concatContent) > self.width / 7:
					concatContent = concatContent[:int(self.width / 7)]
				self.print("\n".join(art.text2art(concatContent, "swan").split("\n")[2:-limit-1])) # type: ignore
				self.print("▀"*self.width)
			if content[0] == 2:
				if len(concatContent) > self.width / 5:
					concatContent = concatContent[:int(self.width / 5)]
				self.print("\n".join(art.text2art(concatContent, "thin").split("\n")[1:-limit])) # type: ignore
				self.print("━"*self.width)
			if content[0] == 3:
				if len(concatContent) > self.width / 3:
					concatContent = concatContent[:int(self.width / 3)]
				self.print("\n".join(art.text2art(concatContent, "cygnet").split("\n")[1:-limit])) # type: ignore
				self.print("─"*self.width)

	def codeBlock(self, content: tuple[Any, str]):
		'''Process a code block  '''
		self.print("\n │ ", end="")
		self.print("\n │ ".join(content[1].split("\n")))

	def definitionList(self, content: list[tuple[list[Inline], list[list[Block]]]]):
		'''Process a definition list '''
		for definition in content:
			#for definition in definitionBlock:
			self.newline()
			for part in definition[0]:
				processpandoc.processInline(part, self)
			self.print("\t:\t:\t", end="")
			for part in definition[1]:
				for partB in part:
					processpandoc.processBlock(partB, self)

	def orderedList(self, content: list[tuple[list[Any], list[Block]]]):
		'''Process an ordered list '''
		for index, bullet in enumerate(content[1]):
			self.print("\n", index+1, end=". ")
			for point in bullet:
				if point["t"] in ["BulletList"]:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)

	def bulletList(self, content: list[list[Block]]):
		'''Process a bulleted list '''
		for bullet in content:
			for point in bullet:
				if point["t"] not in ["BulletList"]:
					self.print("\n- ", end="")
				else:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)

	def table(self, content: tuple[Any, Caption, list[list[Alignment]],
	TableHead, list[TableBody]]):
		'''Process a table '''
		# Any, Caption, list[list[Alignment]], TableHead, list[TableBody]
		# ignore, ignore, align, tableHead, tableBody
		colWidth = str(int(self.width/len(content[2]))-1)
		alignment = {"AlignLeft": "{:<"+colWidth+"."+colWidth+"}",
		"AlignCenter": "{:^"+colWidth+"."+colWidth+"}",
		"AlignRight": "{:>"+colWidth+"."+colWidth+"}",
		"AlignDefault": "{:<"+colWidth+"."+colWidth+"}"}
		self.print()
		self.print("│", end="")
		for index, tableHead in enumerate(content[3]["c"][1][0]["c"][1]):
			headContent = "".join([processpandoc.toPlaintext(headPart) for headPart in tableHead["c"][4]])
			self.print((alignment[content[2][index][0]["t"]]).format(headContent) + "│", end="")
		self.print("\n│", end="")
		for index, _ in enumerate(content[2]):
			self.print((alignment[content[2][index][0]["t"]]).format("─"*self.width) + "┤", end="")
		for tableRow in content[4][0]["c"][3]:
			self.print("\n│", end="")
			for index, tableCol in enumerate(tableRow["c"][1]):
				colContent = "".join([processpandoc.toPlaintext(colPart) for colPart in tableCol["c"][4]])
				self.print((alignment[content[2][index][0]["t"]]).format(colContent) + "│", end="")
		self.print()


	def blockQuote(self, content: list[Block]):
		'''Process a block quote '''
		print("\n ┃ ", end="")
		print("\n ┃ ".join([processpandoc.toPlaintext(block).split("\n") for block in content][0]))


	#########################################
	# INLINE
	#########################################

	def space(self):
		'''Process a space '''
		self.print(" ", end="")

	def emph(self, content: list[Inline]):
		'''Process emphasized text '''
		for newInline in content:
			self.print("_", end="")
			processpandoc.processInline(newInline, self)
			self.print("_", end="")

	def strong(self, content: list[Inline]):
		'''Process strong (bold) text '''
		for newInline in content:
			self.print("*", end="")
			processpandoc.processInline(newInline, self)
			self.print("*", end="")

	def strikeout(self, content: list[Inline]):
		'''Process strikeout (crossed out) text '''
		for newInline in content:
			self.print("-", end="")
			processpandoc.processInline(newInline, self)
			self.print("-", end="")

	def superscript(self, content: list[Inline]):
		'''Process superscript text '''
		for newInline in content:
			processpandoc.processInline(newInline, self)

	def subscript(self, content: list[Inline]):
		'''Process subscript text '''
		for newInline in content:
			processpandoc.processInline(newInline, self)

	def smallCaps(self, content: list[Inline]):
		'''Process small caps text '''
		for newInline in content:
			processpandoc.processInline(newInline, self)

	def quoted(self, content: tuple[Any, list[Inline]]):
		'''Process quoted text '''
		for newInline in content[1]:
			self.print("\'", end="")
			processpandoc.processInline(newInline, self)
			self.print("\'", end="")

	def code(self, content: tuple[Any, str]):
		'''Process code '''
		self.print(" │" + content[1], end="│ ")

	def math(self, content: tuple[Any, str]):
		'''Process math '''
		self.print("Math: " + content[1])


	def note(self, content: list[Block]):
		'''Process a note '''
		for block in content:
			processpandoc.processBlock(block, self)


	def span(self, content: tuple[Any, list[Inline]]):
		'''Process a span '''
		for newInline in content[1]:
			processpandoc.processInline(newInline, self)


	def image(self, content: tuple[Any, Any, tuple[str, str]]):
		'''Process an image '''
		self.catImage(content[-1][0])

	def link(self, content: tuple[Any, list[Inline], tuple[str, str]]):
		'''Process a link '''
		for part in content[1]:
			processpandoc.processInline(part, self)
		self.print(" -> " + content[2][0], end="")

	def hr(self):
		'''Process a hr '''
		self.print("─"*self.width)
