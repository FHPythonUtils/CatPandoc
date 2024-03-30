"""CLI Application
Cat a pandoc json string.
"""

from __future__ import annotations

import argparse
import re
from io import StringIO

import pypandoc
from rich.console import Console
from rich.markdown import Markdown


def pandoc2ansi(file: str, width: int = 79) -> str:
	string = StringIO()
	console = Console(file=string, color_system="truecolor", safe_box=False, width=width)
	pypandoc.ensure_pandoc_installed()
	markdown = Markdown(pypandoc.convert_file(file, "md"))
	console.print(markdown)
	return string.getvalue()

def stripAnsi(string: str) -> str:
	"""Strip ansi codes from a given string.

	Args:
	----
		string (str): string to strip codes from

	Returns:
	-------
		str: plaintext, utf-8 string (safe for writing to files)

	"""
	return re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])").sub("", string)


def pandoc2plain(file: str, width: int = 79) -> str:
	return stripAnsi(pandoc2ansi(file, width))


def handle(args: argparse.Namespace) -> None:
	"""Handle the args and output to the terminal.

	Args:
	----
		args (argparse.Namespace): Args

	"""

	# Open file and convert to JSON
	try:
		pypandoc.convert_text("#test", "json", format="md")  # type: ignore
	except OSError:
		pypandoc.download_pandoc()  # type: ignore

	width = args.width or 79

	# Print to console
	functions = pandoc2ansi, pandoc2plain
	print(functions[args.to_plain](args.file, width))


def cli() -> None:
	"""Parse args from the command line."""
	parser = argparse.ArgumentParser(description="Print md")
	parser.add_argument("file", help="file to render")
	parser.add_argument("--width", help="terminal width", action="store", type=int)
	parser.add_argument("--to-plain", help="convert to plaintext", action="store_true")
	args = parser.parse_args()
	handle(args)


if __name__ == "__main__":
	cli()
