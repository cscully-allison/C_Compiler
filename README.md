## CS 660
## Symbol Table

## Connor Scully-Allison
## Kurt Andersen
# October 19, 2018

## Table of Contents
[Links to other README's](#links) <br>
[Language Features of the Compiler](#language) <br>
[Implementation](#implementation) <br>
[Assumptions Made](#assumptions) <br>
[Dependencies](#dependenciies) <br>
[Restrictions](#restrictions) <br>
[Misc Notes](#misc) <br>

<a name="links"/>

## Links to other README's

[Symbol Table README](./SymbolTable/README.md)

[Lexical Analyzer README](./LexicalAnalizer/README.md)

[Parser README](./Parser/README.md)

<a name="language"/>

## Language Features of the Compiler

Python 3.6 is used for our compiler

<a name="implementation"/>

## Implementation of the symbol table, lexical analyzer, and parser

The symbol table uses a red-black tree to keep the tree balanced. (Grad student requirement)
The lexical analyzer and parser use the PLY library.  It is similar to the yacc/bison library,
but is a derivation for python.

<a name="assumptions"/>

## Assumptions made

?????

<a name="dependencies"/>

## Dependency Installation Instructions

Python version 3.6 is used.
All other dependencies that are used are listed in requirements.txt
	bintrees - gives access to red black trees for the symbol table
	pytest - gives access to automated testing
	ply - gives access to a lexical analyzer and parser similar to yacc/bison

If python is not installed run the following in the command line in a Linux environment:
```
sudo apt-get install python3.6
```
Once python is installed(it includes pip), to ensure all other dependencies are installed run the following:
```
pip install requirements.txt
```

<a name="restrictions"/>

## Restrictions

As of right now, we allow all errors to continue.  Error location is denoted, but parser and lexical analyzer
continue to run for information purposes.

<a name="misc"/>

## Misc Notes


