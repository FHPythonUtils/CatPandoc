"""Convert a pandoc string to ansi
"""
from __future__ import annotations

import os
import urllib.error
import urllib.request
from typing import Any

import art
import catimage
import pygments
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers import get_lexer_by_name

from catpandoc import processpandoc
from catpandoc.pandoc2plain import Pandoc2Plain
from catpandoc.types import Block, Inline

# Constants
FG = "\033[38;5;"
BG = "\033[48;5;"
CLR_FG = "\033[39m"
CLR_BG = "\033[49m"
CLR = "\033[0m"


class Pandoc2Ansi(Pandoc2Plain):
	"""Convert a pandoc string to ansi. Inherits from Pandoc2Plain (no need
	for identical methods - down with code duplication...)
	"""

	def __init__(
		self, width: int = 80, padding: int = 0, baseColour: tuple[int, int, int] = (4, 0, 4)
	):
		self.content = []
		self.width = width - padding * 2
		self.padding = padding
		self.baseColour = baseColour

	#########################################
	# UTIL
	#########################################

	def catImage(self, content: str):
		"""catImage"""
		self.print(CLR)
		try:
			if content.startswith("http"):
				urllib.request.urlretrieve(content, "dowloadedImage")
				content = "dowloadedImage"
			try:
				self.print(catimage.generateHDColour(os.getcwd() + os.sep + content, self.width))
			except FileNotFoundError:
				self.print(content)
		except urllib.error.HTTPError:
			self.print(content)
		self.print(CLR, end="")

	#########################################
	# BLOCK
	#########################################

	def header(self, content: tuple[int, Any, list[Inline]]):
		"""Process a header"""
		self.print("\n", end="")
		concatContent = ""
		headColour = [
			"0",
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (1, 1, 1))),
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (1, 0, 0))),
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, 0))),
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, -1))),
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1))),
			self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))),
		]
		if content[0] > 3:
			self.print(FG + headColour[content[0]], end="")
			for part in content[2]:
				processpandoc.processInline(part, self)
			self.print(CLR, end="")
		else:
			concatContent = "".join([processpandoc.toPlaintext(part) for part in content[2]])
			if any(char in concatContent for char in ["q", "y", "p", "g", "j"]):
				limit = 1
			else:
				limit = 2
			if content[0] == 1:
				if len(concatContent) > self.width / 7:
					concatContent = concatContent[: int(self.width / 7)]
				self.print(
					FG
					+ headColour[content[0]]
					+ "\n".join(
						art.text2art(concatContent, "swan").split("\n")[  # type: ignore
							2 : -limit - 1
						]
					)
				)
				self.print("▀" * self.width + CLR)
			if content[0] == 2:
				if len(concatContent) > self.width / 5:
					concatContent = concatContent[: int(self.width / 5)]
				self.print(
					FG
					+ headColour[content[0]]
					+ "\n".join(art.text2art(concatContent, "thin").split("\n")[1:-limit])
				)  # type: ignore
				self.print("━" * self.width + CLR)
			if content[0] == 3:
				if len(concatContent) > self.width / 3:
					concatContent = concatContent[: int(self.width / 3)]
				self.print(
					FG
					+ headColour[content[0]]
					+ "\n".join(
						art.text2art(concatContent, "cygnet").split("\n")[1:-limit]  # type: ignore
					)
				)
				self.print("─" * self.width + CLR)

	def codeBlock(self, content: tuple[Any, str]):
		"""Process a code block"""
		codeColour = self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1)))
		self.print(FG + codeColour + "\n │ " + CLR_FG, end="")
		try:
			self.print(
				FG
				+ codeColour
				+ " │ ".join(
					[
						CLR_FG
						+ str(
							pygments.highlight(
								line,
								get_lexer_by_name(content[0][1][0]),  # type: ignore
								Terminal256Formatter(),
							)
						)
						+ CLR
						for line in content[1].split("\n")
					]
				)
			)  # type: ignore
		except (IndexError, pygments.util.ClassNotFound):
			self.print(FG + codeColour + "\n │ ".join(content[1].split("\n")) + CLR_FG)

	def definitionList(self, content: list[tuple[list[Inline], list[list[Block]]]]):
		"""Process a definition list"""
		for definition in content:
			# for definition in definitionBlock:
			self.newline()
			self.print(
				FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end=""
			)
			for part in definition[0]:
				processpandoc.processInline(part, self)
			self.print("\t:" + CLR_FG + ":\t", end="")
			for part in definition[1]:
				for partB in part:
					processpandoc.processBlock(partB, self)

	def orderedList(self, content: list[tuple[list[Any], list[Block]]]):
		"""Process an ordered list"""
		self.print(FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end="")
		for index, bullet in enumerate(content[1]):
			self.print("\n", index + 1, end=". ")
			for point in bullet:
				if point["t"] in ["BulletList"]:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)
		self.print(CLR_FG, end="")

	def bulletList(self, content: list[list[Block]]):
		"""Process a bulleted list"""
		self.print(FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -2))), end="")
		for bullet in content:
			for point in bullet:
				if point["t"] not in ["BulletList"]:
					self.print("\n- ", end="")
				else:
					self.print(" > ", end="")
				processpandoc.processBlock(point, self)
		self.print(CLR_FG, end="")

	# Table

	def blockQuote(self, content: list[Block]):
		"""Process a block quote"""
		print(
			"\n" + FG + self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-2, -2, -2))) + " ┃ ",
			end="",
		)
		print(
			"\n ┃ ".join([processpandoc.toPlaintext(block).split("\n") for block in content][0])
			+ CLR_FG
		)

	#########################################
	# INLINE
	#########################################

	# Space

	def emph(self, content: list[Inline]):
		"""Process emphasized text"""
		for newInline in content:
			self.print("\033[3m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[23m", end="")

	def strong(self, content: list[Inline]):
		"""Process strong (bold) text"""
		for newInline in content:
			self.print("\033[1m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[21m", end="")

	def strikeout(self, content: list[Inline]):
		"""Process strikeout (crossed out) text"""
		for newInline in content:
			self.print("\033[9m", end="")
			processpandoc.processInline(newInline, self)
			self.print("\033[29m", end="")

	# Superscript

	# Subscript

	# SmallCaps

	# Quoted

	def code(self, content: tuple[Any, str]):
		"""Process code"""
		self.print(
			FG
			+ self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (-1, -1, -1)))
			+ " │"
			+ content[1],
			end="│ " + CLR_FG,
		)

	# Math

	# Note

	# Span

	# Image

	# Link

	def hr(self):
		"""Process a hr"""
		self.print(
			FG
			+ self.ansiFromAnsiRgb(self.varBaseC(self.baseColour, (0, 0, 0)))
			+ "─" * self.width
			+ CLR_FG
		)

	def ansiFromAnsiRgb(self, colour: tuple[int, int, int]) -> str:
		"""Generates ansi based on reduced rgb ie in range 0-5"""
		red, green, blue = colour
		return (
			str(
				int(
					16 + min(max(red, 0), 5) * 36 + min(max(green, 0), 5) * 6 + min(max(blue, 0), 5)
				)
			)
			+ "m"
		)

	def varBaseC(
		self, base: tuple[int, int, int], modify: tuple[int, int, int]
	) -> tuple[int, int, int]:
		"""Generates a colour based on the theme colour"""
		newC = []
		for index in range(3):
			newC.append(base[index] + modify[index])
		return tuple(newC)  # type: ignore
