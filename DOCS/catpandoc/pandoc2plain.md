# pandoc2plain

> Auto-generated documentation for [catpandoc.pandoc2plain](../../catpandoc/pandoc2plain.py) module.

Convert a pandoc string to plaintext

- [Catpandoc](../README.md#catpandoc-index) / [Modules](../README.md#catpandoc-modules) / [catpandoc](index.md#catpandoc) / pandoc2plain
    - [Pandoc2Plain](#pandoc2plain)
        - [Pandoc2Plain().blockQuote](#pandoc2plainblockquote)
        - [Pandoc2Plain().bulletList](#pandoc2plainbulletlist)
        - [Pandoc2Plain().catImage](#pandoc2plaincatimage)
        - [Pandoc2Plain().code](#pandoc2plaincode)
        - [Pandoc2Plain().codeBlock](#pandoc2plaincodeblock)
        - [Pandoc2Plain().definitionList](#pandoc2plaindefinitionlist)
        - [Pandoc2Plain().emph](#pandoc2plainemph)
        - [Pandoc2Plain().genOutput](#pandoc2plaingenoutput)
        - [Pandoc2Plain().header](#pandoc2plainheader)
        - [Pandoc2Plain().hr](#pandoc2plainhr)
        - [Pandoc2Plain().image](#pandoc2plainimage)
        - [Pandoc2Plain().link](#pandoc2plainlink)
        - [Pandoc2Plain().math](#pandoc2plainmath)
        - [Pandoc2Plain().newline](#pandoc2plainnewline)
        - [Pandoc2Plain().note](#pandoc2plainnote)
        - [Pandoc2Plain().orderedList](#pandoc2plainorderedlist)
        - [Pandoc2Plain().print](#pandoc2plainprint)
        - [Pandoc2Plain().quoted](#pandoc2plainquoted)
        - [Pandoc2Plain().smallCaps](#pandoc2plainsmallcaps)
        - [Pandoc2Plain().space](#pandoc2plainspace)
        - [Pandoc2Plain().span](#pandoc2plainspan)
        - [Pandoc2Plain().strikeout](#pandoc2plainstrikeout)
        - [Pandoc2Plain().strong](#pandoc2plainstrong)
        - [Pandoc2Plain().subscript](#pandoc2plainsubscript)
        - [Pandoc2Plain().superscript](#pandoc2plainsuperscript)
        - [Pandoc2Plain().table](#pandoc2plaintable)

## Pandoc2Plain

[[find in source code]](../../catpandoc/pandoc2plain.py#L15)

```python
class Pandoc2Plain(pandoc2xyz.Pandoc2XYZ):
    def __init__(width: int = 80, padding: int = 0):
```

Convert a pandoc string to plaintext

### Pandoc2Plain().blockQuote

[[find in source code]](../../catpandoc/pandoc2plain.py#L155)

```python
def blockQuote(content: list[Block]):
```

Process a block quote

### Pandoc2Plain().bulletList

[[find in source code]](../../catpandoc/pandoc2plain.py#L119)

```python
def bulletList(content: list[list[Block]]):
```

Process a bulleted list

### Pandoc2Plain().catImage

[[find in source code]](../../catpandoc/pandoc2plain.py#L32)

```python
def catImage(content: str):
```

catImage

### Pandoc2Plain().code

[[find in source code]](../../catpandoc/pandoc2plain.py#L212)

```python
def code(content: tuple[(Any, str)]):
```

Process code

### Pandoc2Plain().codeBlock

[[find in source code]](../../catpandoc/pandoc2plain.py#L93)

```python
def codeBlock(content: tuple[(Any, str)]):
```

Process a code block

### Pandoc2Plain().definitionList

[[find in source code]](../../catpandoc/pandoc2plain.py#L98)

```python
def definitionList(content: list[tuple[(list[Inline], list[list[Block]])]]):
```

Process a definition list

### Pandoc2Plain().emph

[[find in source code]](../../catpandoc/pandoc2plain.py#L169)

```python
def emph(content: list[Inline]):
```

Process emphasized text

### Pandoc2Plain().genOutput

[[find in source code]](../../catpandoc/pandoc2plain.py#L52)

```python
def genOutput() -> str:
```

Generate output

### Pandoc2Plain().header

[[find in source code]](../../catpandoc/pandoc2plain.py#L64)

```python
def header(content: tuple[(int, Any, list[Inline])]):
```

Process a header

### Pandoc2Plain().hr

[[find in source code]](../../catpandoc/pandoc2plain.py#L243)

```python
def hr():
```

Process a hr

### Pandoc2Plain().image

[[find in source code]](../../catpandoc/pandoc2plain.py#L233)

```python
def image(content: tuple[(Any, Any, tuple[(str, str)])]):
```

Process an image

### Pandoc2Plain().link

[[find in source code]](../../catpandoc/pandoc2plain.py#L237)

```python
def link(content: tuple[(Any, list[Inline], tuple[(str, str)])]):
```

Process a link

### Pandoc2Plain().math

[[find in source code]](../../catpandoc/pandoc2plain.py#L216)

```python
def math(content: tuple[(Any, str)]):
```

Process math

### Pandoc2Plain().newline

[[find in source code]](../../catpandoc/pandoc2plain.py#L28)

```python
def newline():
```

newline

### Pandoc2Plain().note

[[find in source code]](../../catpandoc/pandoc2plain.py#L221)

```python
def note(content: list[Block]):
```

Process a note

### Pandoc2Plain().orderedList

[[find in source code]](../../catpandoc/pandoc2plain.py#L110)

```python
def orderedList(content: list[tuple[(list[Any], list[Block])]]):
```

Process an ordered list

### Pandoc2Plain().print

[[find in source code]](../../catpandoc/pandoc2plain.py#L47)

```python
def print(end: str = '\n', *args: object) -> None:
```

Define a custom print method that has a very similar signature
to the inbuilt print method

### Pandoc2Plain().quoted

[[find in source code]](../../catpandoc/pandoc2plain.py#L205)

```python
def quoted(content: tuple[(Any, list[Inline])]):
```

Process quoted text

### Pandoc2Plain().smallCaps

[[find in source code]](../../catpandoc/pandoc2plain.py#L200)

```python
def smallCaps(content: list[Inline]):
```

Process small caps text

### Pandoc2Plain().space

[[find in source code]](../../catpandoc/pandoc2plain.py#L165)

```python
def space():
```

Process a space

### Pandoc2Plain().span

[[find in source code]](../../catpandoc/pandoc2plain.py#L227)

```python
def span(content: tuple[(Any, list[Inline])]):
```

Process a span

### Pandoc2Plain().strikeout

[[find in source code]](../../catpandoc/pandoc2plain.py#L183)

```python
def strikeout(content: list[Inline]):
```

Process strikeout (crossed out) text

### Pandoc2Plain().strong

[[find in source code]](../../catpandoc/pandoc2plain.py#L176)

```python
def strong(content: list[Inline]):
```

Process strong (bold) text

### Pandoc2Plain().subscript

[[find in source code]](../../catpandoc/pandoc2plain.py#L195)

```python
def subscript(content: list[Inline]):
```

Process subscript text

### Pandoc2Plain().superscript

[[find in source code]](../../catpandoc/pandoc2plain.py#L190)

```python
def superscript(content: list[Inline]):
```

Process superscript text

### Pandoc2Plain().table

[[find in source code]](../../catpandoc/pandoc2plain.py#L129)

```python
def table(
    content: tuple[(
        Any,
        Caption,
        list[list[Alignment]],
        tuple[(
            Any,
            tuple[tuple[(Any, tuple[(Any, Any, Any, Any, list[TableHead])])]],
        )],
        tuple[(Any, Any, Any, Any, tuple[tuple[(Any, Any, Any, TableBody)]])],
    )],
):
```

Process a table
