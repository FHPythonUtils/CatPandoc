
from pathlib import Path

from catpandoc import application

THISDIR = str(Path(__file__).resolve().parent)



def test_pandoc2ansi():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.md")
	# Path(f"{THISDIR}/test_data/catpandoc.ansi").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc.ansi").read_text("utf-8")

def test_pandoc2plain():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.md")
	# Path(f"{THISDIR}/test_data/catpandoc.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc.txt").read_text("utf-8")

def test_pandoc2plain_docx():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.docx")
	# Path(f"{THISDIR}/test_data/catpandoc_docx.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc_docx.txt").read_text("utf-8")

def test_pandoc2plain_html():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.html")
	# Path(f"{THISDIR}/test_data/catpandoc_html.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc_html.txt").read_text("utf-8")

def test_pandoc2plain_latex():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.latex")
	# Path(f"{THISDIR}/test_data/catpandoc_latex.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc_latex.txt").read_text("utf-8")

def test_pandoc2plain_rst():
	fmt = application.pandoc2ansi(f"{THISDIR}/test_data/catpandoc.rst")
	# Path(f"{THISDIR}/test_data/catpandoc_rst.txt").write_text(fmt, "utf-8")
	assert fmt == Path(f"{THISDIR}/test_data/catpandoc_rst.txt").read_text("utf-8")
