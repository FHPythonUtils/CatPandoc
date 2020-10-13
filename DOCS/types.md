Module catpandoc.types
======================
Types

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

Classes
-------

`Alignment(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `t: str`
    :

`Block(*args, **kwargs)`
:   Block

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: Any`
    :

    `t: str`
    :

`Caption(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: list[Any]`
    :

    `t: str`
    :

`Cell(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: tuple[Any, dict[str, str], dict[str, str], dict[str, str], list[Inline]]`
    :

    `t: str`
    :

`Content(*args, **kwargs)`
:   Content

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: Any`
    :

    `t: str`
    :

`Inline(*args, **kwargs)`
:   Inline

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: Any`
    :

    `t: str`
    :

`Row(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: tuple[Any, list[Cell]]`
    :

    `t: str`
    :

`TableBody(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: tuple[Any, Any, Any, list[Row]]`
    :

    `t: str`
    :

`TableHead(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `c: list[list[Row]]`
    :

    `t: str`
    :