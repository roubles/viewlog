# viewlog

viewlog is a command line tool to browse and historical versions of files stored using git, and open them in vi|vim|mvim|gvim. 

The terminal browser is a looping picker that shows up as follows:
```
$ viewlog rmed
 Pick your git commit id

 => 20000e5e59270e99bc134b9acade8c722cc410de - 34 hours ago, rouble blessed the code thusly: kitchen sink
    8c0d5009b69afeca06333b8efd3a4690b92f64f5 - 34 hours ago, rouble blessed the code thusly: major architectural changes
    f8b2265944f10a4de3de3113bdb654b22c4fb65f - 34 hours ago, rouble blessed the code thusly: Preparing for FCS
    ae45df5ea466778a62da394370854ed49833696a - 35 hours ago, rouble blessed the code thusly: what me worry?
    eafce9c6d5e742c59da35daeaffdd681a9ba8d14 - 35 hours ago, rouble blessed the code thusly: rewrote from scratch again
    0f2d343409a843b14861d385fd000440eb1360ca - 35 hours ago, rouble blessed the code thusly: rewrote from scratch 
    5e61aa5dce263bdfd6adf0a3bca34d9ab66fbf08 - 2 days ago, rouble blessed the code thusly: would you believe, more features?
    e1a61f877c085dd79b863c0664007fc2c9880bda - 2 days ago, chuck norris blessed the code thusly: more features again
    8b10be72399c66a51462e7c8cd801b726ea6bab9 - 2 days ago, jackie chan blessed the code thusly: even more features
    f1711513272d8e1dda0db73f1f491c7a575c2f91 - 3 days ago, rajnikant blessed the code thusly: More features
    next page
    exit
```

Obligatory animated gif:
![alt tag](https://raw.github.com/roubles/viewlog/master/doc/viewlog.gif)

## Hat tip
Hat tip to Wong2 for the [pick](https://github.com/wong2/pick) library that was used for the curses picker implementation.

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

## Install
It's really just one python file that you can store in your path. There is a standard install script.
```
$ git clone https://github.com/roubles/viewlog
$ cd viewlog
$ ./install.py
```

## Custom editor
You can use your own editor:
```
$ viewlog <filename> --editor [mvim|gvim]
```
The operating system emacs is not supported, mostly because I can't get it read from stdin, and has nothing to do with the fact that I don't think its a good editor.
