"""Call functions in catpandoc to output cli2gui.md with an increased width
and "fancy" theme
"""
from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import ctypes
import json
import platform

import pypandoc

from catpandoc import pandoc2ansi, processpandoc

# Fix terminal for windows
if platform.system() == "Windows":
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

output = json.loads(pypandoc.convert_file(THISDIR + "/cli2gui.md", "json"))
for block in output["blocks"]:
	pandoc = pandoc2ansi.Pandoc2Ansi()
	processpandoc.processBlock(block, pandoc)
	print(pandoc.genOutput())
