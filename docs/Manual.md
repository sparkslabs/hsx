# HSX Manual

This describes behaviour as per Version 0.0.3

Since this is a leading "0", this is an experimental version and only applies to this release.

## Core Usage


Recall current usage:

> hsx [OPTIONS]

* `--dir <directory>       ` Fragment directory
* `--extension <ext>       ` Fragment file extension
* `--destfile <filename>   ` Write output to file instead of stdout
* `--file <filename>       ` Filename to process

### Worked Example

If we walk through one of the examples.

> cd examples/simple_example
> hsx

Since this is run with no arguments the options take the following defaults:

| `--dir` | Not provided, so defaults to `_fragx/` |
| `--extension` | defaults to `.hsx` |
| `--destfile` | Writes to stdout |
| `--file` | defaults to `markdown.hsx` |

Note: Not all of these make sense at the moment.


