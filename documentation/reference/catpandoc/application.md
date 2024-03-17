# Application

[Catpandoc Index](../README.md#catpandoc-index) / [Catpandoc](./index.md#catpandoc) / Application

> Auto-generated documentation for [catpandoc.application](../../../catpandoc/application.py) module.

- [Application](#application)
  - [cli](#cli)
  - [handle](#handle)
  - [pandoc2ansi](#pandoc2ansi)
  - [pandoc2plain](#pandoc2plain)

## cli

[Show source in application.py:52](../../../catpandoc/application.py#L52)

Parse args from the command line.

#### Signature

```python
def cli() -> None: ...
```



## handle

[Show source in application.py:30](../../../catpandoc/application.py#L30)

Handle the args and output to the terminal.

#### Arguments

----
 - `args` *argparse.Namespace* - Args

#### Signature

```python
def handle(args: argparse.Namespace) -> None: ...
```



## pandoc2ansi

[Show source in application.py:14](../../../catpandoc/application.py#L14)

#### Signature

```python
def pandoc2ansi(file: str, width: int = 79) -> str: ...
```



## pandoc2plain

[Show source in application.py:22](../../../catpandoc/application.py#L22)

#### Signature

```python
def pandoc2plain(file: str, width: int = 79) -> str: ...
```