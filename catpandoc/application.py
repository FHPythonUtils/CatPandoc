"""CLI Application
Cat a pandoc json string.
"""

from __future__ import annotations

import argparse

import pypandoc
from rich.console import Console
from rich.markdown import Markdown


def pandoc2ansi(file: str, width: int = 79) -> str:
	console = Console(width=width)
	markdown = Markdown(pypandoc.convert_file(file, "md"))
	with console.capture() as capture:
		console.print(markdown)
	return capture.get()


def pandoc2plain(file: str, width: int = 79) -> str:
	console = Console(color_system=None, width=width)
	markdown = Markdown(pypandoc.convert_file(file, "md"))
	with console.capture() as capture:
		console.print(markdown)
	return capture.get()


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
