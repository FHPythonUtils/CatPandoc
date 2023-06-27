# Application

[Catpandoc Index](../README.md#catpandoc-index) /
[Catpandoc](./index.md#catpandoc) /
Application

> Auto-generated documentation for [catpandoc.application](../../../catpandoc/application.py) module.

- [Application](#application)
  - [cli](#cli)
  - [handle](#handle)
  - [pandoc2ansi](#pandoc2ansi)
  - [pandoc2plain](#pandoc2plain)

## cli

[Show source in application.py:49](../../../catpandoc/application.py#L49)

Parse args from the command line

#### Signature

```python
def cli() -> None:
    ...
```



## handle

[Show source in application.py:29](../../../catpandoc/application.py#L29)

Handle the args and output to the terminal

#### Arguments

- `args` *argparse.Namespace* - Args

#### Signature

```python
def handle(args: argparse.Namespace):
    ...
```



## pandoc2ansi

[Show source in application.py:13](../../../catpandoc/application.py#L13)

#### Signature

```python
def pandoc2ansi(file: str, width: int = 79) -> str:
    ...
```



## pandoc2plain

[Show source in application.py:21](../../../catpandoc/application.py#L21)

#### Signature

```python
def pandoc2plain(file: str, width: int = 79) -> str:
    ...
```


