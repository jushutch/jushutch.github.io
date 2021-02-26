## Flag #4
Difficulty: Hard  
Flag: MHCTF{intr0_t0_steg0}

This is the first flag that utilizes steganography, or hiding messages in media. The first challenge is figuring out which
images might be suspicious or interesting to look at. In this case, there is a relatively small number of images which makes
the process pretty quick, but when there are hundreds of images, it's quicker to write a short script to test them all. The
first tool to use on any file is the "strings" command, which prints all the strings in a file. This command can be 
combined with "grep" to limit output to any strings matching a specific pattern. The command used to discover this flag
is:  
<code>strings headshot.png | grep "MHCTF"</code>  
  
The flag was hidden by creating a text file "flag.txt" and appending it to the end of "headshot.png":  
<code>cat flag.txt >> headshot.png</code>  
The "flag.txt" step can be skipped using the following command, but the file is an easy way to remember the flag:
<code>echo "MHCTF{intr0_t0_steg0}" >> headshot.png</code>
