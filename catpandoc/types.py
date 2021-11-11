"""
Types

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

from typing import Any, TypedDict


class Inline(TypedDict):
	"""Inline"""

	t: str
	c: Any


class Block(TypedDict):
	"""Block"""

	t: str
	c: Any


class Content(TypedDict):
	"""Content"""

	t: str
	c: Any


class Caption(TypedDict):
	t: str
	c: list[Any]


class Alignment(TypedDict):
	t: str


class Cell(TypedDict):
	t: str
	c: tuple[Any, dict[str, str], dict[str, str], dict[str, str], list[Inline]]


class Row(TypedDict):
	t: str
	c: tuple[Any, list[Cell]]


class TableHead(TypedDict):
	t: str
	c: list[list[Row]]


class TableBody(TypedDict):
	t: str
	c: tuple[Any, Any, Any, list[Row]]
