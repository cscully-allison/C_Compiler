# CS 660
# PA 5, 6, 7, 8: Symbol Table, Lexical Analyzer, Parser, Abstarct Syntax Tree

# Connor Scully-Allison and Kurt Andersen
### October 19, 2018

## Table of Contents
[Links to other README's](#links) <br>
[Language Features of the Compiler](#language) <br>
[Implementation](#implementation) <br>
[Assumptions Made](#assumptions) <br>
[Dependencies](#dependenciies) <br>
[Restrictions](#restrictions) <br>
[Misc Notes](#misc) <br>

<a name="links"/>

## Links to Wiki and other README's

[Project Wiki](https://www.github.com/cscully-allison/C_Compilier/wiki/CS-660:-Connor-Scully-Allison-and-Kurt-Andersen) <br>
[Symbol Table README](./SymbolTable/) <br>
[Lexical Analyzer README](./LexicalAnalizer/) <br>
[Parser README / Abstract Syntax Tree / 3AC](./Parser/) <br>

<a name="language"/>

## Language Features of the Compiler

Python 3.6 is used for our compiler

<a name="implementation"/>

## Implementation of the symbol table, lexical analyzer, and parser

The symbol table uses a red-black tree to keep the tree balanced. (Grad student requirement)

The lexical analyzer and parser use the PLY library.  It is similar to the yacc/bison library,
but is a derivation for python.

NOTE: No external token file is used or reuired by PLY. Instead tokens are defined as a tuple of strings which can be found in [LexicalAnalizer.py](./Parser/LexicalAnalizer.py)

<a name="assumptions"/>

## Assumptions made

We are under the assumption that a single line of code stays within the 4095 character length.

We check for max length of an identifier for being less than 31 characters.

<a name="dependencies"/>

## Dependency Installation Instructions

Python version 3.6 is used.
All other dependencies that are used are listed in requirements.txt

	bintrees - gives access to red black trees for the symbol table

	pytest - gives access to automated testing

	ply - gives access to a lexical analyzer and parser similar to yacc/bison
	
	graphviz

	anytree

If python is not installed run the following in the command line in a Linux environment:
```
sudo apt-get install python3.6
```
Once python is installed(it includes pip), to ensure all other dependencies are installed run the following:
```
pip install -r requirements.txt
```

<a name="restrictions"/>

## Restrictions

Syntax errors will stop the compiler when it occurs.  The error location is described to the user.

Warnings will display the location of the warning and detailed information about the warning.



<a name="misc"/>

## Misc Notes
