"""CLI Application
Cat a pandoc json string
"""
from __future__ import annotations
from sys import stdout

import json
import argparse
import pypandoc

from catpandoc import pandoc2plain, pandoc2ansi, processpandoc

stdout.reconfigure(encoding="utf-8") # type: ignore


def handle(args: argparse.Namespace):
	"""Handle the args and output to the terminal

	Args:
		args (argparse.Namespace): Args
	"""


	# Open file and convert to JSON
	try:
		pypandoc.convert_text("#test", "json", format='md') # type: ignore
	except (FileNotFoundError, OSError):
		pypandoc.download_pandoc() # type: ignore
	output = json.loads(pypandoc.convert_file(args.file, 'json')) # type: ignore

	# Process args
	width = 80
	padding = 0
	if args.width is not None:
		width = int(args.width)
	if args.padding is not None:
		padding = int(args.padding)
	theme = (4, 0, 4)
	if args.theme is not None:
		try:
			themeList = [int(col) for col in args.theme.split(",")]
			theme: tuple[int, int, int] = tuple(themeList)[:3] # type: ignore
		except (IndexError, ValueError):
			theme = (4, 0, 4)

	# Print to console
	if args.to_plain:
		pandoc = pandoc2plain.Pandoc2Plain(width, padding)
		for block in output["blocks"]:
			processpandoc.processBlock(block, pandoc)
		print(pandoc.genOutput())
	else:
		pandoc = pandoc2ansi.Pandoc2Ansi(width, padding, theme)
		for block in output["blocks"]:
			processpandoc.processBlock(block, pandoc)
		print(pandoc.genOutput())


def cli() -> None:
	"""Parse args from the command line
	"""
	parser = argparse.ArgumentParser(description="Print md")
	parser.add_argument("file", help="file to render")
	parser.add_argument("--width", help="terminal width", action="store")
	parser.add_argument("--padding", help="terminal padding", action="store")
	parser.add_argument("--theme", help="theme to use r,g,b 0-5", action="store")
	parser.add_argument("--to-ansi", help="convert to ansi", action="store_true")
	parser.add_argument("--to-plain", help="convert to plaintext", action="store_true")
	args = parser.parse_args()
	handle(args)

if __name__ == "__main__":
	cli()
