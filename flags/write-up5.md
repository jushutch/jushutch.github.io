## Flag #5
Difficulty: Hard  
Flag: MHCTF{n0thing_t0_s33_h3r3}

This is the second flag that utilizes steganography, or hiding messages in media. One of the challenges that makes this 
flag harder to find is that it's hidden in the favicon of the page. It's not as easy to download and requires using the 
browser debugger and examining the network tab. Refreshing the page will show when the favicon is loaded, and inspecting the request
will allow the image to be downloaded. Once the image is downloaded, one should run the "strings" command and realize that 
nothing interesting shows up. The reason is that the flag has been compressed before being added to the image. The best tool
to use in this situation is "binwalk", which is available with most package managers. This tool can walk through the image
data and find all types of hidden files and folders, and extract the hidden files into a separate folder. For this flag, one would
run:  
<code>binwalk -e logo.png</code>  
This reveals that there was a hidden zip folder and extracts it to a new directory. Looking at the files in this directory,
one can quickly find the flag.
  
This flag was hidden similarly as the last flag, but "flag.txt" was compressed with "tar" before being appended.
