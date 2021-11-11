"""Convert a pandoc string to plaintext
"""
from __future__ import annotations

from typing import Any

from catpandoc.types import Alignment, Block, Caption, Inline, TableBody, TableHead


class Pandoc2XYZ:
	"""Dummy for typing"""

	def __init__(self, width: int = 80, padding: int = 0):
		pass

	#########################################
	# UTIL
	#########################################

	def newline(self):
		"""newline"""

	def catImage(self, content: str):
		"""catImage"""

	def print(self, *args: object, end: str = "\n") -> None:
		"""Define a custom print method that has a very similar signature
		to the inbuilt print method"""

	def genOutput(self) -> str:
		"""Generate output"""

	#########################################
	# BLOCK
	#########################################

	def header(self, content: tuple[int, Any, list[Inline]]):
		"""Process a header"""

	def codeBlock(self, content: tuple[Any, str]):
		"""Process a code block"""

	def definitionList(self, content: list[tuple[list[Inline], list[list[Block]]]]):
		"""Process a definition list"""

	def orderedList(self, content: list[tuple[list[Any], list[Block]]]):
		"""Process an ordered list"""

	def bulletList(self, content: list[list[Block]]):
		"""Process a bulleted list"""

	def table(
		self, content: tuple[Any, Caption, list[list[Alignment]], TableHead, list[TableBody]]
	):
		"""Process a table"""
		# inline[], alignment[], double[], tablecell[], tablecell[][]
		# ignore. align, ignore, tableHead, tableBody

	def blockQuote(self, content: list[Block]):
		"""Process a block quote"""

	#########################################
	# INLINE
	#########################################

	def space(self):
		"""Process a space"""

	def emph(self, content: list[Inline]):
		"""Process emphasized text"""

	def strong(self, content: list[Inline]):
		"""Process strong (bold) text"""

	def strikeout(self, content: list[Inline]):
		"""Process strikeout (crossed out) text"""

	def superscript(self, content: list[Inline]):
		"""Process superscript text"""

	def subscript(self, content: list[Inline]):
		"""Process subscript text"""

	def smallCaps(self, content: list[Inline]):
		"""Process small caps text"""

	def quoted(self, content: tuple[Any, list[Inline]]):
		"""Process quoted text"""

	def code(self, content: tuple[Any, str]):
		"""Process code"""

	def math(self, content: tuple[Any, str]):
		"""Process math"""

	def note(self, content: list[Block]):
		"""Process a note"""

	def span(self, content: tuple[Any, list[Inline]]):
		"""Process a span"""

	def image(self, content: tuple[Any, Any, tuple[str, str]]):
		"""Process an image"""

	def link(self, content: tuple[Any, list[Inline], tuple[str, str]]):
		"""Process a link"""

	def hr(self):
		"""Process a hr"""
