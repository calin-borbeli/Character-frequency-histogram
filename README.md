# Character frequency histogram

Displays how often (or how rare) each letter appears in the text.

Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

A program which:

- asks the user for the input file's name;

- reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)

- prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Assuming that the test file contains just one line filled with:

`aBabBc`

the expected output should look as follows:

`
a -> 2
b -> 3
c -> 1
`
