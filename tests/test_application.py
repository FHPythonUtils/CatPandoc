from pathlib import Path
from typing import Callable

from catpandoc import application

THISDIR = str(Path(__file__).resolve().parent)


def _aux_test_func(pandoc_func: Callable, doc: str, compare_doc: str) -> bool:
	fmt = pandoc_func(doc)
	# Path(compare_doc).write_text(fmt, "utf-8")
	assert fmt == Path(compare_doc).read_text("utf-8")


def test_pandoc2ansi() -> None:
	_aux_test_func(
		pandoc_func=application.pandoc2ansi,
		doc=f"{THISDIR}/data/catpandoc.md",
		compare_doc=f"{THISDIR}/data/catpandoc.ansi",
	)


def test_pandoc2plain() -> None:
	_aux_test_func(
		pandoc_func=application.pandoc2plain,
		doc=f"{THISDIR}/data/catpandoc.md",
		compare_doc=f"{THISDIR}/data/catpandoc.txt",
	)


def test_pandoc2ansi_docx() -> None:
	_aux_test_func(
		pandoc_func=application.pandoc2ansi,
		doc=f"{THISDIR}/data/catpandoc.docx",
		compare_doc=f"{THISDIR}/data/catpandoc_docx.txt",
	)


def test_pandoc2ansi_html() -> None:
	_aux_test_func(
		pandoc_func=application.pandoc2ansi,
		doc=f"{THISDIR}/data/catpandoc.html",
		compare_doc=f"{THISDIR}/data/catpandoc_html.txt",
	)


def test_pandoc2ansi_latex() -> None:
	_aux_test_func(
		application.pandoc2plain,
		doc=f"{THISDIR}/data/catpandoc.latex",
		compare_doc=f"{THISDIR}/data/catpandoc_latex.txt",
	)


def test_pandoc2ansi_rst() -> None:
	_aux_test_func(
		application.pandoc2plain,
		doc=f"{THISDIR}/data/catpandoc.rst",
		compare_doc=f"{THISDIR}/data/catpandoc_rst.txt",
	)
