htx
===

htx is a small macro-style preprocessor for static content.

It replaces XML-like tags in a source file with the contents of fragment
files stored in a directory.

Fragments are plain text files (for example markdown, HTML, CSS) and are
included by tag name.

## Author

Michael Sparks (sparks.m@gmail.com / <https://github.com/sparkslabs> )

## What it does

Replaces `<Tag />` with the contents of `Tag.<extension>` from a fragment
directory.

* Supports attributes: `<Tag key="value" />` with `{args.key}` substitution.

* Supports block tags: `<Tag> ...  </Tag>` with `{args.__text__}` substitution.

* Supports nested tags.

* Evaluates fragments recursively with a bounded recursion depth.

Deliberately fails on structural mismatches (eg  misordered closing tags). 
It does not implement loops, conditionals, or a templating language.


## Usage

Assuming copied onto your path somewhere

> htx.py

> htx.py [OPTIONS]

Where options are:

* `--dir <directory>       ` Fragment directory
* `--extension <ext>       ` Fragment file extension
* `--destfile <filename>   ` Write output to file instead of stdout
* `--file <filename>       ` Filename to process

Defaults:

* Fragment directory: `frags`

* Fragment extension: `.hsx`

* Source file: `markdown.hsx`



## License

Apache License 2.0 (as usual)


