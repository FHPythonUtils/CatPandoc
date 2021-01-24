# pandoc2ansi

> Auto-generated documentation for [catpandoc.pandoc2ansi](../../catpandoc/pandoc2ansi.py) module.

Convert a pandoc string to ansi

- [Catpandoc](../README.md#catpandoc-index) / [Modules](../README.md#catpandoc-modules) / [catpandoc](index.md#catpandoc) / pandoc2ansi
    - [Pandoc2Ansi](#pandoc2ansi)
        - [Pandoc2Ansi().ansiFromAnsiRgb](#pandoc2ansiansifromansirgb)
        - [Pandoc2Ansi().blockQuote](#pandoc2ansiblockquote)
        - [Pandoc2Ansi().bulletList](#pandoc2ansibulletlist)
        - [Pandoc2Ansi().catImage](#pandoc2ansicatimage)
        - [Pandoc2Ansi().code](#pandoc2ansicode)
        - [Pandoc2Ansi().codeBlock](#pandoc2ansicodeblock)
        - [Pandoc2Ansi().definitionList](#pandoc2ansidefinitionlist)
        - [Pandoc2Ansi().emph](#pandoc2ansiemph)
        - [Pandoc2Ansi().header](#pandoc2ansiheader)
        - [Pandoc2Ansi().hr](#pandoc2ansihr)
        - [Pandoc2Ansi().orderedList](#pandoc2ansiorderedlist)
        - [Pandoc2Ansi().strikeout](#pandoc2ansistrikeout)
        - [Pandoc2Ansi().strong](#pandoc2ansistrong)
        - [Pandoc2Ansi().varBaseC](#pandoc2ansivarbasec)

#### Attributes

- `FG` - Constants: `'\x1b[38;5;'`

## Pandoc2Ansi

[[find in source code]](../../catpandoc/pandoc2ansi.py#L28)

```python
class Pandoc2Ansi(Pandoc2Plain):
    def __init__(
        width: int = 80,
        padding: int = 0,
        baseColour: tuple[(int, int, int)] = (4, 0, 4),
    ):
```

Convert a pandoc string to ansi. Inherits from Pandoc2Plain (no need
for identical methods - down with code duplication...)

#### See also

- [Pandoc2Plain](pandoc2plain.md#pandoc2plain)

### Pandoc2Ansi().ansiFromAnsiRgb

[[find in source code]](../../catpandoc/pandoc2ansi.py#L231)

```python
def ansiFromAnsiRgb(colour: tuple[(int, int, int)]) -> str:
```

Generates ansi based on reduced rgb ie in range 0-5

### Pandoc2Ansi().blockQuote

[[find in source code]](../../catpandoc/pandoc2ansi.py#L165)

```python
def blockQuote(content: list[Block]):
```

Process a block quote

### Pandoc2Ansi().bulletList

[[find in source code]](../../catpandoc/pandoc2ansi.py#L149)

```python
def bulletList(content: list[list[Block]]):
```

Process a bulleted list

### Pandoc2Ansi().catImage

[[find in source code]](../../catpandoc/pandoc2ansi.py#L43)

```python
def catImage(content: str):
```

catImage

### Pandoc2Ansi().code

[[find in source code]](../../catpandoc/pandoc2ansi.py#L209)

```python
def code(content: tuple[(Any, str)]):
```

Process code

### Pandoc2Ansi().codeBlock

[[find in source code]](../../catpandoc/pandoc2ansi.py#L108)

```python
def codeBlock(content: tuple[(Any, str)]):
```

Process a code block

### Pandoc2Ansi().definitionList

[[find in source code]](../../catpandoc/pandoc2ansi.py#L121)

```python
def definitionList(content: list[tuple[(list[Inline], list[list[Block]])]]):
```

Process a definition list

### Pandoc2Ansi().emph

[[find in source code]](../../catpandoc/pandoc2ansi.py#L180)

```python
def emph(content: list[Inline]):
```

Process emphasized text

### Pandoc2Ansi().header

[[find in source code]](../../catpandoc/pandoc2ansi.py#L63)

```python
def header(content: tuple[(int, Any, list[Inline])]):
```

Process a header

### Pandoc2Ansi().hr

[[find in source code]](../../catpandoc/pandoc2ansi.py#L225)

```python
def hr():
```

Process a hr

### Pandoc2Ansi().orderedList

[[find in source code]](../../catpandoc/pandoc2ansi.py#L136)

```python
def orderedList(content: list[tuple[(list[Any], list[Block])]]):
```

Process an ordered list

### Pandoc2Ansi().strikeout

[[find in source code]](../../catpandoc/pandoc2ansi.py#L194)

```python
def strikeout(content: list[Inline]):
```

Process strikeout (crossed out) text

### Pandoc2Ansi().strong

[[find in source code]](../../catpandoc/pandoc2ansi.py#L187)

```python
def strong(content: list[Inline]):
```

Process strong (bold) text

### Pandoc2Ansi().varBaseC

[[find in source code]](../../catpandoc/pandoc2ansi.py#L238)

```python
def varBaseC(
    base: tuple[(int, int, int)],
    modify: tuple[(int, int, int)],
) -> tuple[(int, int, int)]:
```

Generates a colour based on the theme colour
