"""Holds functions to iterate through the pandoc json

Block
	Plain
	Para
	LineBlock
	CodeBlock
	RawBlock
	BlockQuote
	OrderedList
	BulletList
	DefinitionList
	Header
	HorizontalRule
	Table
	Div
	Null


Inline
	Str
	Emph
	Strong
	Strikeout
	Superscript
	Subscript
	SmallCaps
	Quoted
	Cite
	Code
	Space
	SoftBreak
	LineBreak
	Math
	RawInline
	Link
	Image
	Note
	Span


"""
from __future__ import annotations

import re

import emoji

from catpandoc import pandoc2xyz
from catpandoc.types import Block, Inline


def toPlaintext(inline: Inline) -> str:
	"""Convert an inline or block to plain text

	Args:
		inline (Inline): An inline holds various types such as 'Space', 'Bold'
		and other Inlines

	Returns:
		string: plain text
	"""
	if inline["t"] == "Space":
		return " "
	if inline["t"] == "Str":
		# text
		return emoji.emojize(inline["c"])
	if inline["t"] in ["Emph", "Strong", "Strikeout", "Superscript", "Subscript", "SmallCaps"]:
		# inline[]
		text = []
		for newInline in inline["c"]:
			text.append(toPlaintext(newInline))
		return "".join(text)
	if inline["t"] == "Quoted":
		# quotetype, inline[]
		text = []
		for newInline in inline["c"][1]:
			text.append("'" + toPlaintext(newInline) + "'")
		return "".join(text)
	if inline["t"] == "Code":
		return " │" + inline["c"][1] + " │ "
	if inline["t"] in ["Plain", "Para"]:
		# inline[]
		text = []
		for newInline in inline["c"]:
			text.append(toPlaintext(newInline))
		return "".join(text)
	if inline["t"] in ["SoftBreak", "LineBreak"]:
		return "\n"
	if inline["t"] == "Link":
		return inline["c"][2][0]
	if inline["t"] == "RawInline":
		return inline["c"][1]
	print(inline)
	raise RuntimeError


def processRaw(content: tuple[str, str], pandoc2: pandoc2xyz.Pandoc2XYZ):
	"""Process raw data - this might be html

	Args:
		content (tuple[str, str]): content type and content data
		pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter
	"""
	if content[0] in ["html"]:
		if content[1].startswith("<img"):
			pandoc2.catImage(re.findall(r"src=\"(.*?)\"", content[1])[0])
		elif content[1].startswith("<!--"):
			pass
		else:
			pandoc2.print(content)
	else:
		pandoc2.print(content)


def processInline(inline: Inline, pandoc2: pandoc2xyz.Pandoc2XYZ):
	"""Do stuff for an inline object

	Args:
		inline (Inline): An inline holds various types such as 'Space', 'Bold'
		and other Inlines
		pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter
	"""
	if inline["t"] == "Str":
		# text
		pandoc2.print(emoji.emojize(inline["c"]), end="")
	if inline["t"] == "Emph":
		# inline[]
		pandoc2.emph(inline["c"])
	if inline["t"] == "Strong":
		# inline[]
		pandoc2.strong(inline["c"])
	if inline["t"] == "Strikeout":
		# inline[]
		pandoc2.strikeout(inline["c"])
	if inline["t"] == "Superscript":
		# inline[]
		pandoc2.superscript(inline["c"])
	if inline["t"] == "Subscript":
		# inline[]
		pandoc2.subscript(inline["c"])
	if inline["t"] == "SmallCaps":
		# inline[]
		pandoc2.smallCaps(inline["c"])
	if inline["t"] == "Quoted":
		# quotetype, inline[]
		pandoc2.quoted(inline["c"])
	if inline["t"] == "Cite":
		# citation[], inline[]
		# TODO
		# pandoc2.cite(inline["c"])
		pass
	if inline["t"] == "Code":
		# attributes, text
		pandoc2.code(inline["c"])
	if inline["t"] == "Space":
		pandoc2.space()
	if inline["t"] == "SoftBreak":
		pandoc2.newline()
	if inline["t"] == "LineBreak":
		pandoc2.newline()
	if inline["t"] == "Math":
		# mathtype, text
		pandoc2.math(inline["c"])
	if inline["t"] == "RawInline":
		# format, text
		processRaw(inline["c"], pandoc2)
	if inline["t"] == "Link":
		# attr, inline[], text
		pandoc2.link(inline["c"])
	if inline["t"] == "Image":
		# attr, inline[], text
		pandoc2.image(inline["c"])
	if inline["t"] == "Note":
		# block[]
		pandoc2.note(inline["c"])
	if inline["t"] == "Span":
		# attr, inline[]
		pandoc2.span(inline["c"])


def processBlock(block: Block, pandoc2: pandoc2xyz.Pandoc2XYZ) -> None:
	"""Do stuff for an block object

	Args:
		block (Block): An block holds various types such as 'Para', 'Table'
		pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter
	"""
	if block["t"] == "Plain":
		# inline[]
		for inline in block["c"]:
			processInline(inline, pandoc2)
	if block["t"] == "Para":
		# inline[]
		for inline in block["c"]:
			processInline(inline, pandoc2)
		pandoc2.newline()
	if block["t"] == "LineBlock":
		# inline[][]
		# TODO
		# pandoc2.lineBlock(block["c"])
		pass
	if block["t"] == "CodeBlock":
		# language, text
		pandoc2.codeBlock(block["c"])
	if block["t"] == "RawBlock":
		# type, text
		processRaw(block["c"], pandoc2)
	if block["t"] == "BlockQuote":
		# block[]
		pandoc2.blockQuote(block["c"])
	if block["t"] == "OrderedList":
		# attributes, block[][]
		pandoc2.orderedList(block["c"])
		pandoc2.newline()
	if block["t"] == "BulletList":
		# block[][]
		pandoc2.bulletList(block["c"])
		pandoc2.newline()

	if block["t"] == "DefinitionList":
		# [key, value] key=inline[] value=block[]
		pandoc2.definitionList(block["c"])
	if block["t"] == "Header":
		# int, attr, inline[]
		pandoc2.header(block["c"])
	if block["t"] == "HorizontalRule":
		pandoc2.hr()
	if block["t"] == "Table":
		# inline[], alignment[], double[], tablecell[], tablecell[][]
		# ignore. align, ignore, tableHead, tableBody
		pandoc2.table(block["c"])
	if block["t"] == "Div":
		# attr, block[]
		for newBlock in block["c"][1]:
			processBlock(newBlock, pandoc2)
	if block["t"] == "Null":
		pass
