# Tag Sort
A simple script to sort/group text-blocks according to their tags.

## How to use
The script uses python3 and is simply called with '''python tag_sort'''. It searches for a file named input.txt.
input.txt is then parsed and processed. 

The script parses the file line by line.
A header/title (e.g. the name of an interviewed person) for the next text blocks is alwasy a empty line, the header line and one ore more empty lines again.

Every textblock has a simple structure:

'''
<empty line>
Header od the Textblock as plaintext in one line
### As many tags as you wish
### preceeded by three hastags
The long, long textblock
containing the statement or 
any thing else you want to sort/group with
this script
<empty line>
'''

A textblock is alwas surrounded by empty lines, the first line is a header, all following lines containing three hastags are tags and al the text until the next empty line is the content of the textblock.

The script will parse the whole input.txt. Then it will create a folder named output and for every tag it finds it creates a file in that folder. A single file contains the Name of the tag and every Textblock including it's header, and it's main header. Like this:

'''
Name of the Tag

Main Header 1
SubHeader 1
The textblock for subheader 1...

Main Header 1
SubHeader 2
The textblock for subheader 2...

Main Header 4
SubHeader 7
The textblock for subheader 4.7...
'''

Of course it will only contain the textblocks, that were marked with that tag in the input.txt
