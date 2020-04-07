document.write("Hello World from JavaScript!<br>")
names = ["Chester", "aRthuR", "OlivEr", "QUINN", "MAlcolm"];

for (i = 0; i < names.length; ++i) {
  names[i] = names[i].charAt(0).toUpperCase() + names[i].substr(1).toLowerCase();
  document.write(names[i] + "<br>");
}