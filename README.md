# viewlog

viewlog is a command line tool to browse and view historical versions of files stored using git. Obligatory animated gif:
![alt tag](https://raw.github.com/rouble/viewlog/master/doc/viewlog.gif)



## Motivation
I know there are lots of git gui's out there. But I like terminals. Maybe I am oldschool. I was getting by with this bash function for a while:
```
vimgitshow() { git show "$1" | vim - "+set filetype=${1##*.}"; }
```
... but then I decided to slap some code together and broswe the history
