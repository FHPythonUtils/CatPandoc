Module catpandoc.processpandoc
==============================
Holds functions to iterate through the pandoc json

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

Functions
---------

    
`processBlock(block: Block, pandoc2: pandoc2xyz.Pandoc2XYZ) ‑> NoneType`
:   Do stuff for an block object
    
    Args:
            block (Block): An block holds various types such as 'Para', 'Table'
            pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter

    
`processInline(inline: Inline, pandoc2: pandoc2xyz.Pandoc2XYZ)`
:   Do stuff for an inline object
    
    Args:
            inline (Inline): An inline holds various types such as 'Space', 'Bold'
            and other Inlines
            pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter

    
`processRaw(content: tuple[str, str], pandoc2: pandoc2xyz.Pandoc2XYZ)`
:   Process raw data - this might be html
    
    Args:
            content (tuple[str, str]): content type and content data
            pandoc2 (pandoc2xyz.Pandoc2XYZ): pandoc2XYZ object formatter

    
`toPlaintext(inline: Inline) ‑> str`
:   Convert an inline or block to plain text
    
    Args:
            inline (Inline): An inline holds various types such as 'Space', 'Bold'
            and other Inlines
    
    Returns:
            string: plain text