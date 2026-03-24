hsx
===
**Version:** 0.0.1

hsx is (will be) a small macro-style preprocessor for static content.

It replaces XML-like tags in a source file with the contents of fragment
files stored in a directory.

Fragments are plain text files (for example markdown, HTML, CSS) and are
composited using JSX like instructions.

## Code Maturity

This code is experimental, and version 0.0.1
See SEMVER.md for how I use semantic versioning


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

> hsx.py

> hsx.py [OPTIONS]

Where options are:

* `--dir <directory>       ` Fragment directory
* `--extension <ext>       ` Fragment file extension
* `--destfile <filename>   ` Write output to file instead of stdout
* `--file <filename>       ` Filename to process

Defaults:

* Fragment directory: `frags`

* Fragment extension: `.hsx`

* Source file: `markdown.hsx`


# Bonus mkAutoSite.py

mkAutoSite is intended to use hsx - in particular it's designed to
statically compile a collection of templates, HSX files, and markdown files
to a static website.

This is put here for the moment as an expediency to eradicate having 10
copies across my filesystem.

# Plan for Autosite

Extend current template processing to build templates from HSX files



## License

Apache License 2.0 (as usual)


