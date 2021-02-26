## Flag #3
Difficulty: Medium  
Flag: MHCTF{welcome}

This flag was hidden as separate html encoded characters throughout home.html. The idea here is that text can be written
in a variety of ways, binary, hex, html codes, etc. and to pay close attention to the source code. The Microsoft Edge
debugger actually highlights each of the html codes in red, which makes them much easier to spot. Otherwise, one could 
search for all the strings that start with "&#", which identifies html encoding. Then it's simply translating each 
character or using the context of the word it was embedded in to put the flag together.
