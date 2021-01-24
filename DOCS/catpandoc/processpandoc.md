# processpandoc

> Auto-generated documentation for [catpandoc.processpandoc](../../catpandoc/processpandoc.py) module.

Holds functions to iterate through the pandoc json

- [Catpandoc](../README.md#catpandoc-index) / [Modules](../README.md#catpandoc-modules) / [catpandoc](index.md#catpandoc) / processpandoc
    - [processBlock](#processblock)
    - [processInline](#processinline)
    - [processRaw](#processraw)
    - [toPlaintext](#toplaintext)

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

## processBlock

[[find in source code]](../../catpandoc/processpandoc.py#L179)

```python
def processBlock(block: Block, pandoc2: pandoc2xyz.Pandoc2XYZ) -> None:
```

Do stuff for an block object

#### Arguments

- `block` *Block* - An block holds various types such as 'Para', 'Table'
- `pandoc2` *pandoc2xyz.Pandoc2XYZ* - pandoc2XYZ object formatter

#### See also

- [Block](types.md#block)

## processInline

[[find in source code]](../../catpandoc/processpandoc.py#L114)

```python
def processInline(inline: Inline, pandoc2: pandoc2xyz.Pandoc2XYZ):
```

Do stuff for an inline object

#### Arguments

- `inline` *Inline* - An inline holds various types such as 'Space', 'Bold'
and other Inlines
- `pandoc2` *pandoc2xyz.Pandoc2XYZ* - pandoc2XYZ object formatter

#### See also

- [Inline](types.md#inline)

## processRaw

[[find in source code]](../../catpandoc/processpandoc.py#L97)

```python
def processRaw(content: tuple[(str, str)], pandoc2: pandoc2xyz.Pandoc2XYZ):
```

Process raw data - this might be html

#### Arguments

content (tuple[str, str]): content type and content data
- `pandoc2` *pandoc2xyz.Pandoc2XYZ* - pandoc2XYZ object formatter

## toPlaintext

[[find in source code]](../../catpandoc/processpandoc.py#L51)

```python
def toPlaintext(inline: Inline) -> str:
```

Convert an inline or block to plain text

#### Arguments

- `inline` *Inline* - An inline holds various types such as 'Space', 'Bold'
and other Inlines

#### Returns

- `string` - plain text

#### See also

- [Inline](types.md#inline)
