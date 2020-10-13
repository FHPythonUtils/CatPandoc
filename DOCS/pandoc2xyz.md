Module catpandoc.pandoc2xyz
===========================
Convert a pandoc string to plaintext

Classes
-------

`Pandoc2XYZ(width: int = 80, padding: int = 0)`
:   Dummy for typing

    ### Descendants

    * catpandoc.pandoc2plain.Pandoc2Plain

    ### Methods

    `blockQuote(self, content: list[Block])`
    :   Process a block quote

    `bulletList(self, content: list[list[Block]])`
    :   Process a bulleted list

    `catImage(self, content: str)`
    :   catImage

    `code(self, content: tuple[Any, str])`
    :   Process code

    `codeBlock(self, content: tuple[Any, str])`
    :   Process a code block

    `definitionList(self, content: list[tuple[list[Inline], list[list[Block]]]])`
    :   Process a definition list

    `emph(self, content: list[Inline])`
    :   Process emphasized text

    `genOutput(self) ‑> str`
    :   Generate output

    `header(self, content: tuple[int, Any, list[Inline]])`
    :   Process a header

    `hr(self)`
    :   Process a hr

    `image(self, content: tuple[Any, Any, tuple[str, str]])`
    :   Process an image

    `link(self, content: tuple[Any, list[Inline], tuple[str, str]])`
    :   Process a link

    `math(self, content: tuple[Any, str])`
    :   Process math

    `newline(self)`
    :   newline

    `note(self, content: list[Block])`
    :   Process a note

    `orderedList(self, content: list[tuple[list[Any], list[Block]]])`
    :   Process an ordered list

    `print(self, *args: object, end: str = '\n') ‑> NoneType`
    :   Define a custom print method that has a very similar signature
        to the inbuilt print method

    `quoted(self, content: tuple[Any, list[Inline]])`
    :   Process quoted text

    `smallCaps(self, content: list[Inline])`
    :   Process small caps text

    `space(self)`
    :   Process a space

    `span(self, content: tuple[Any, list[Inline]])`
    :   Process a span

    `strikeout(self, content: list[Inline])`
    :   Process strikeout (crossed out) text

    `strong(self, content: list[Inline])`
    :   Process strong (bold) text

    `subscript(self, content: list[Inline])`
    :   Process subscript text

    `superscript(self, content: list[Inline])`
    :   Process superscript text

    `table(self, content: tuple[Any, Caption, list[list[Alignment]], TableHead, list[TableBody]])`
    :   Process a table