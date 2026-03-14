#!/bin/python

# This tool is turning into something I use more and more often it seems
# It should probably be "better" engineered...

import os

def slurp(filename,binary=False, encoding="utf-8"):
    """Utility to slurp a file from the filesystem"""
    print("OPEN:", filename)
    f = open(filename, "rb")
    x = f.read()
    if not binary:
        x = x.decode(encoding)
    f.close()
    return x

def store(filename, contents, binary=False):
    """Stores the given contents to a file on the filesystem"""
    if not binary:
        f = open(filename, "w")
    else:
        f = open(filename, "wb")
    f.write(contents)
    f.close()

# Unix like tools - copy, find, head

def copy(source, dest):
    """Slurp and Store"""
    data = slurp(source, binary=True)
    store(dest, data, binary=True)

def find(basedir, t="file"):
    """"Iterator that operates like 'find . -type f' under linux/etc"""
    if t != "file":
        # In theory we could support other types of things we're interested in.
        # In practice, we're not.
        raise NotImplementedError()

    for i in os.listdir(basedir):
        p = os.path.join(basedir, i)
        if os.path.isdir(p):  # Descend into directories, and traverse depth first
            for j in find(p, t):
                yield j
        else:
            yield p

def head(count, gen):
    for i in range(count):
        yield next(gen)




def ensureTargetDirectoryExists(config):
    # Ensure target directory exists
    # destdir = os.path.join(config['target'], config["resources"])
    try:
        os.makedirs(config["destdir"])
    except FileExistsError:
        pass

def copy_static_resources(config):
    # Copy the site-resources into the target directory
    for entry in find(config["resources"]):
        if entry.endswith("~"):
            continue
        filename = os.path.basename(entry)
        print("BASENAME:",os.path.basename(entry))
        print("DIRNAME:",os.path.dirname(entry))
        print("TARGET:",config["destdir"])
        print("SOURCE:", config["resources"])
        target_dir = config["destdir"].replace(config["resources"], os.path.dirname(entry))
        try:
            os.makedirs(target_dir)
        except FileExistsError:
            pass

        target_filename = os.path.join(target_dir, filename)
        print("COPY", entry, target_filename)
        copy(entry, target_filename)
        print("------------")


def createHTMLPagesFromMarkdownTree(config):
    source = config['source']
    target = config['target']
    tld_default = pagetemplate = slurp(f"{config['resources']}/page-template.html")

    pandoc_command_template = 'pandoc --from markdown+backtick_code_blocks+grid_tables --to html --highlight-style kate %(source)s -o %(dest)s'

    for entry in find(source):
        if not entry.endswith(".md"):
            continue
        filename = entry.replace("markdown/","")
        print(f"Processed {filename}")

        # Ensure the target directory exists for the given filename.
        basename = os.path.basename(filename)
        dirname = os.path.dirname(filename)        # D=$(dirname $filename)
        print("chtmlfrommd:DIRNAME", repr(dirname))
        if dirname:
            try:
                pagetemplate = slurp(os.path.join(config['resources'], os.path.join(config['source'], f"{dirname}/page-template.html")))
                print(f"SLURPED: {dirname}/page-template.html")
            except FileNotFoundError:
                print(f"FAILED SLURP {config['resources']}/{dirname}/page-template.html")
                pagetemplate = tld_default
        # pagetemplate = slurp(f"{config['resources']}/page-template.html")

        tdirname = os.path.join(target, dirname)
        try:
            os.makedirs(tdirname)                # cd ../auto-site/ ; mkdir -p $D
        except FileExistsError:
            pass
        print("os.makedirs(tdirname)", tdirname)

        # Run the markdown through pandoc to get the content. We create the target page iteratively.
        # We could pull in fields from the markdown+yaml file to throw into the template.
        # We don't do that right now

        corename = basename[:-3]                  # basename=`echo $filename | sed -e "s/.md$//g" ` # strip ".md"
        target_filename = os.path.join(tdirname, corename)+".html"

        command = pandoc_command_template % { "source": entry, "dest" : target_filename }
        print(command)
        os.system(command)
        print()

        sourcepage = slurp(target_filename)
        newpage = pagetemplate.replace("%CONTENT GOES HERE%", sourcepage)
        store(target_filename, newpage)

def buildSite(config):
    ensureTargetDirectoryExists(config)
    copy_static_resources(config)
    createHTMLPagesFromMarkdownTree(config)

if __name__ == "__main__":
    config = {
                "source" : "markdown",
                "target" : "auto-site",
                "resources" : "site-resources",
             }
    config["destdir"] = os.path.join(config['target'], config["resources"])

    buildSite(config)
