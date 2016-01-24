# viewlog

viewlog is a command line tool to browse and view historical versions of files stored using git in vim. 
```
 Pick your git commit id

 => 20000e5e59270e99bc134b9acade8c722cc410de - 34 hours ago, Pranab Mehta blessed the code thusly: bugfixes
    8c0d5009b69afeca06333b8efd3a4690b92f64f5 - 34 hours ago, Pranab Mehta blessed the code thusly: bugfixes
    f8b2265944f10a4de3de3113bdb654b22c4fb65f - 34 hours ago, Pranab Mehta blessed the code thusly: Preparing for FCS
    ae45df5ea466778a62da394370854ed49833696a - 35 hours ago, Pranab Mehta blessed the code thusly: bugfixes
    eafce9c6d5e742c59da35daeaffdd681a9ba8d14 - 35 hours ago, Pranab Mehta blessed the code thusly: bugfixes
    0f2d343409a843b14861d385fd000440eb1360ca - 35 hours ago, Pranab Mehta blessed the code thusly: bugfixes
    5e61aa5dce263bdfd6adf0a3bca34d9ab66fbf08 - 2 days ago, Pranab Mehta blessed the code thusly: bufixes
    e1a61f877c085dd79b863c0664007fc2c9880bda - 2 days ago, Pranab Mehta blessed the code thusly: more features
    8b10be72399c66a51462e7c8cd801b726ea6bab9 - 2 days ago, Pranab Mehta blessed the code thusly: More features.
    f1711513272d8e1dda0db73f1f491c7a575c2f91 - 3 days ago, Pranab Mehta blessed the code thusly: More features
    next page
    exit
```

Obligatory animated gif:
![alt tag](https://raw.github.com/roubles/viewlog/master/doc/viewlog.gif)

## Motivation
I know there are lots of git gui's out there. But I like terminals. Maybe I am oldschool. I was getting by with this bash function for a while:
```
vimgitshow() { git show "$1" | vim - "+set filetype=${1##*.}"; }
```
... but then I decided to slap some code together and browse the history and use vim to open the files.

## Usage
```
usage: viewlog [-h] [-e EDITOR] [-s SKIP] [-l LIMIT] [-f LOGFORMAT] filename

terminal git log broswer

positional arguments:
  filename              Path to filename

optional arguments:
  -h, --help            show this help message and exit
  -e EDITOR, --editor EDITOR
                        Editor to use
  -s SKIP, --skip SKIP  Starting commit offset
  -l LIMIT, --limit LIMIT
                        Total commits to show
  -f LOGFORMAT, --logformat LOGFORMAT
                        Pretty format for git commit
```
