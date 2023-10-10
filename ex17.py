from sys import argv
from os.path import exists
script, from_file, to_file = argv

#combined into one line
#first open 'to_file' as 'w' to declare that we are writing to this document.
#.write as a function call and within the call, read from the 'from_file' and write it to the 'to_file'
open(to_file, 'w').write(open(from_file).read())
