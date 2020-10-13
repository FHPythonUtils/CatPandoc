Module catpandoc.pandoc2ansi
============================
Convert a pandoc string to ansi

Classes
-------

`Pandoc2Ansi(width: int = 80, padding: int = 0, baseColour: tuple[int, int, int] = (4, 0, 4))`
:   Convert a pandoc string to ansi. Inherits from Pandoc2Plain (no need
    for identical methods - down with code duplication...)

    ### Ancestors (in MRO)

    * catpandoc.pandoc2plain.Pandoc2Plain
    * catpandoc.pandoc2xyz.Pandoc2XYZ

    ### Methods

    `ansiFromAnsiRgb(self, colour: tuple[int, int, int]) ‑> str`
    :   Generates ansi based on reduced rgb ie in range 0-5

    `varBaseC(self, base: tuple[int, int, int], modify: tuple[int, int, int]) ‑> tuple[int, int, int]`
    :   Generates a colour based on the theme colour