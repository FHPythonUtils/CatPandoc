"""CLI Application
Cat a pandoc json string
"""

import json
import argparse
import platform
import ctypes
from cli2gui import Cli2Gui
import pypandoc
from catpandoc import pandoc2plain, pandoc2ansi, processpandoc


def handle(args):
	"""Handle the args and output to the terminal

	Args:
		args (argparse.Namespace): Args
	"""
	# Fix terminal for windows
	if platform.system() == "Windows":
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

	# Open file and convert to JSON
	try:
		pypandoc.convert_text("#test", "json", format='md')
	except (FileNotFoundError, OSError):
		pypandoc.download_pandoc()
	output = json.loads(pypandoc.convert_file(args.file, 'json'))

	# Process args
	width = 80
	padding = 0
	if args.width is not None:
		width = int(args.width)
	if args.padding is not None:
		padding = int(args.padding)
	theme = (4, 0, 4)
	if args.theme is not None:
		theme = tuple([int(col) for col in args.theme.split(",")])

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


@Cli2Gui(run_function=handle)
def cli():
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
