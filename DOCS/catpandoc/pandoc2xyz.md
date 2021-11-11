# pandoc2xyz

> Auto-generated documentation for [catpandoc.pandoc2xyz](../../catpandoc/pandoc2xyz.py) module.

Convert a pandoc string to plaintext

- [Catpandoc](../README.md#catpandoc-index) / [Modules](../README.md#catpandoc-modules) / [catpandoc](index.md#catpandoc) / pandoc2xyz
    - [Pandoc2XYZ](#pandoc2xyz)
        - [Pandoc2XYZ().blockQuote](#pandoc2xyzblockquote)
        - [Pandoc2XYZ().bulletList](#pandoc2xyzbulletlist)
        - [Pandoc2XYZ().catImage](#pandoc2xyzcatimage)
        - [Pandoc2XYZ().code](#pandoc2xyzcode)
        - [Pandoc2XYZ().codeBlock](#pandoc2xyzcodeblock)
        - [Pandoc2XYZ().definitionList](#pandoc2xyzdefinitionlist)
        - [Pandoc2XYZ().emph](#pandoc2xyzemph)
        - [Pandoc2XYZ().genOutput](#pandoc2xyzgenoutput)
        - [Pandoc2XYZ().header](#pandoc2xyzheader)
        - [Pandoc2XYZ().hr](#pandoc2xyzhr)
        - [Pandoc2XYZ().image](#pandoc2xyzimage)
        - [Pandoc2XYZ().link](#pandoc2xyzlink)
        - [Pandoc2XYZ().math](#pandoc2xyzmath)
        - [Pandoc2XYZ().newline](#pandoc2xyznewline)
        - [Pandoc2XYZ().note](#pandoc2xyznote)
        - [Pandoc2XYZ().orderedList](#pandoc2xyzorderedlist)
        - [Pandoc2XYZ().print](#pandoc2xyzprint)
        - [Pandoc2XYZ().quoted](#pandoc2xyzquoted)
        - [Pandoc2XYZ().smallCaps](#pandoc2xyzsmallcaps)
        - [Pandoc2XYZ().space](#pandoc2xyzspace)
        - [Pandoc2XYZ().span](#pandoc2xyzspan)
        - [Pandoc2XYZ().strikeout](#pandoc2xyzstrikeout)
        - [Pandoc2XYZ().strong](#pandoc2xyzstrong)
        - [Pandoc2XYZ().subscript](#pandoc2xyzsubscript)
        - [Pandoc2XYZ().superscript](#pandoc2xyzsuperscript)
        - [Pandoc2XYZ().table](#pandoc2xyztable)

## Pandoc2XYZ

[[find in source code]](../../catpandoc/pandoc2xyz.py#L10)

```python
class Pandoc2XYZ():
    def __init__(width: int = 80, padding: int = 0):
```

Dummy for typing

### Pandoc2XYZ().blockQuote

[[find in source code]](../../catpandoc/pandoc2xyz.py#L59)

```python
def blockQuote(content: list[Block]):
```

Process a block quote

### Pandoc2XYZ().bulletList

[[find in source code]](../../catpandoc/pandoc2xyz.py#L49)

```python
def bulletList(content: list[list[Block]]):
```

Process a bulleted list

### Pandoc2XYZ().catImage

[[find in source code]](../../catpandoc/pandoc2xyz.py#L23)

```python
def catImage(content: str):
```

catImage

### Pandoc2XYZ().code

[[find in source code]](../../catpandoc/pandoc2xyz.py#L90)

```python
def code(content: tuple[(Any, str)]):
```

Process code

### Pandoc2XYZ().codeBlock

[[find in source code]](../../catpandoc/pandoc2xyz.py#L40)

```python
def codeBlock(content: tuple[(Any, str)]):
```

Process a code block

### Pandoc2XYZ().definitionList

[[find in source code]](../../catpandoc/pandoc2xyz.py#L43)

```python
def definitionList(content: list[tuple[(list[Inline], list[list[Block]])]]):
```

Process a definition list

### Pandoc2XYZ().emph

[[find in source code]](../../catpandoc/pandoc2xyz.py#L69)

```python
def emph(content: list[Inline]):
```

Process emphasized text

### Pandoc2XYZ().genOutput

[[find in source code]](../../catpandoc/pandoc2xyz.py#L30)

```python
def genOutput() -> str:
```

Generate output

### Pandoc2XYZ().header

[[find in source code]](../../catpandoc/pandoc2xyz.py#L37)

```python
def header(content: tuple[(int, Any, list[Inline])]):
```

Process a header

### Pandoc2XYZ().hr

[[find in source code]](../../catpandoc/pandoc2xyz.py#L108)

```python
def hr():
```

Process a hr

### Pandoc2XYZ().image

[[find in source code]](../../catpandoc/pandoc2xyz.py#L102)

```python
def image(content: tuple[(Any, Any, tuple[(str, str)])]):
```

Process an image

### Pandoc2XYZ().link

[[find in source code]](../../catpandoc/pandoc2xyz.py#L105)

```python
def link(content: tuple[(Any, list[Inline], tuple[(str, str)])]):
```

Process a link

### Pandoc2XYZ().math

[[find in source code]](../../catpandoc/pandoc2xyz.py#L93)

```python
def math(content: tuple[(Any, str)]):
```

Process math

### Pandoc2XYZ().newline

[[find in source code]](../../catpandoc/pandoc2xyz.py#L20)

```python
def newline():
```

newline

### Pandoc2XYZ().note

[[find in source code]](../../catpandoc/pandoc2xyz.py#L96)

```python
def note(content: list[Block]):
```

Process a note

### Pandoc2XYZ().orderedList

[[find in source code]](../../catpandoc/pandoc2xyz.py#L46)

```python
def orderedList(content: list[tuple[(list[Any], list[Block])]]):
```

Process an ordered list

### Pandoc2XYZ().print

[[find in source code]](../../catpandoc/pandoc2xyz.py#L26)

```python
def print(end: str = '\n', *args: object) -> None:
```

Define a custom print method that has a very similar signature
to the inbuilt print method

### Pandoc2XYZ().quoted

[[find in source code]](../../catpandoc/pandoc2xyz.py#L87)

```python
def quoted(content: tuple[(Any, list[Inline])]):
```

Process quoted text

### Pandoc2XYZ().smallCaps

[[find in source code]](../../catpandoc/pandoc2xyz.py#L84)

```python
def smallCaps(content: list[Inline]):
```

Process small caps text

### Pandoc2XYZ().space

[[find in source code]](../../catpandoc/pandoc2xyz.py#L66)

```python
def space():
```

Process a space

### Pandoc2XYZ().span

[[find in source code]](../../catpandoc/pandoc2xyz.py#L99)

```python
def span(content: tuple[(Any, list[Inline])]):
```

Process a span

### Pandoc2XYZ().strikeout

[[find in source code]](../../catpandoc/pandoc2xyz.py#L75)

```python
def strikeout(content: list[Inline]):
```

Process strikeout (crossed out) text

### Pandoc2XYZ().strong

[[find in source code]](../../catpandoc/pandoc2xyz.py#L72)

```python
def strong(content: list[Inline]):
```

Process strong (bold) text

### Pandoc2XYZ().subscript

[[find in source code]](../../catpandoc/pandoc2xyz.py#L81)

```python
def subscript(content: list[Inline]):
```

Process subscript text

### Pandoc2XYZ().superscript

[[find in source code]](../../catpandoc/pandoc2xyz.py#L78)

```python
def superscript(content: list[Inline]):
```

Process superscript text

### Pandoc2XYZ().table

[[find in source code]](../../catpandoc/pandoc2xyz.py#L52)

```python
def table(
    content: tuple[(Any, Caption, list[list[Alignment]], TableHead, list[TableBody])],
):
```

Process a table
