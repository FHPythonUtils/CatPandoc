# Application

[Catpandoc Index](../README.md#catpandoc-index) / [Catpandoc](./index.md#catpandoc) / Application

> Auto-generated documentation for [catpandoc.application](../../../catpandoc/application.py) module.

- [Application](#application)
  - [cli](#cli)
  - [handle](#handle)
  - [pandoc2ansi](#pandoc2ansi)
  - [pandoc2plain](#pandoc2plain)
  - [stripAnsi](#stripansi)

## cli

[Show source in application.py:65](../../../catpandoc/application.py#L65)

Parse args from the command line.

#### Signature

```python
def cli() -> None: ...
```



## handle

[Show source in application.py:43](../../../catpandoc/application.py#L43)

Handle the args and output to the terminal.

#### Arguments

----
 - `args` *argparse.Namespace* - Args

#### Signature

```python
def handle(args: argparse.Namespace) -> None: ...
```



## pandoc2ansi

[Show source in application.py:16](../../../catpandoc/application.py#L16)

#### Signature

```python
def pandoc2ansi(file: str, width: int = 79) -> str: ...
```



## pandoc2plain

[Show source in application.py:39](../../../catpandoc/application.py#L39)

#### Signature

```python
def pandoc2plain(file: str, width: int = 79) -> str: ...
```



## stripAnsi

[Show source in application.py:24](../../../catpandoc/application.py#L24)

Strip ansi codes from a given string.

#### Arguments

----
 - `string` *str* - string to strip codes from

#### Returns

-------
 - `str` - plaintext, utf-8 string (safe for writing to files)

#### Signature

```python
def stripAnsi(string: str) -> str: ...
```