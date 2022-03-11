# Application

> Auto-generated documentation for [catpandoc.application](../../../catpandoc/application.py) module.

CLI Application
Cat a pandoc json string

- [Catpandoc](../README.md#catpandoc-index) / [Modules](../MODULES.md#catpandoc-modules) / [Catpandoc](index.md#catpandoc) / Application
    - [cli](#cli)
    - [handle](#handle)
    - [pandoc2ansi](#pandoc2ansi)
    - [pandoc2plain](#pandoc2plain)

## cli

[[find in source code]](../../../catpandoc/application.py#L47)

```python
def cli() -> None:
```

Parse args from the command line

## handle

[[find in source code]](../../../catpandoc/application.py#L29)

```python
def handle(args: argparse.Namespace):
```

Handle the args and output to the terminal

#### Arguments

- `args` *argparse.Namespace* - Args

## pandoc2ansi

[[find in source code]](../../../catpandoc/application.py#L13)

```python
def pandoc2ansi(file: str, width: int) -> str:
```

## pandoc2plain

[[find in source code]](../../../catpandoc/application.py#L21)

```python
def pandoc2plain(file: str, width: int) -> str:
```
