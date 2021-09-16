## Flag #6
Difficulty: Easy  
Flag: MHCTF{mast3r_insp3ct0r}

This flag is written in the image file flag.png, which is contained in a hidden img tag on index.html. There are
many ways to find the flag, including:

- Removing the hidden attribute on the img tag and viewing the image on the home page

- Inspecting the page and looking in either the sources tab or the network tab to see that flag.png was loaded.
The image can then be seen in the developer tools window.

- Finding the img tag and navigating directly to images/flag.png to see the flag
