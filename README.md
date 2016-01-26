# viewlog

viewlog is a command line tool to browse historical versions of files stored using git, and open it in [less](https://en.wikipedia.org/wiki/Less_(Unix)) (or any editor of your choice). 

More technically, viewlog is a terminal based git log browser that allows you to cycle through all your git commits. On selection, it will open that version of file in any editor. Here is a sample screen:
```
$ viewlog ~/git/rmed/sh/rmed
 Pick your git commit id (choose 'exit' or ctrl-c to quit)
 File: /Users/prmehta/git/rmed/sh/rmed

 => 20000e5e59270e99bc134b9acade8c722cc410de - 4 days ago, Rajnikant blessed the code thusly: rewrote from scratch.
    8c0d5009b69afeca06333b8efd3a4690b92f64f5 - 4 days ago, Chuck Norris blessed the code thusly: obliterated all bugs.
    f8b2265944f10a4de3de3113bdb654b22c4fb65f - 4 days ago, Bernie Sanders blessed the code thusly: raised taxes.
    ae45df5ea466778a62da394370854ed49833696a - 4 days ago, Jackie Chan blessed the code thusly: karate chopped bugs.
    eafce9c6d5e742c59da35daeaffdd681a9ba8d14 - 4 days ago, The Hulk blessed the code thusly: smashed bugs.
    0f2d343409a843b14861d385fd000440eb1360ca - 4 days ago, rouble blessed the code thusly: did I mention, more features?
    5e61aa5dce263bdfd6adf0a3bca34d9ab66fbf08 - 4 days ago, rouble blessed the code thusly: more features.
    e1a61f877c085dd79b863c0664007fc2c9880bda - 5 days ago, rouble blessed the code thusly: more features.
    8b10be72399c66a51462e7c8cd801b726ea6bab9 - 5 days ago, rouble blessed the code thusly: more features.
    f1711513272d8e1dda0db73f1f491c7a575c2f91 - 6 days ago, r0uble blessed the code thusly: more features.
    next page
    exit

```

## Install
If you have pip, one line install:
```
$ pip install viewlog
```
or
```
$ git clone https://github.com/roubles/viewlog
$ cd viewlog
$ python setup.py install
```
Note that viewlog is dependent on the pypi package 'pick'. If it doesn't automatically get installed, you need to:
```
$ pip install pick
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
usage: viewlog [-h] [-e EDITOR] [-s SKIP] [-l LIMIT] [-f LOGFORMAT]
               [-b BRANCH] [-n] [-a AFTER] [-u BEFORE] [-k]
               filename

terminal git log browser

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
  -b BRANCH, --branch BRANCH
                        Branch to use
  -n, --nomerges        Do not include commits from merged branches (Default:
                        false)
  -a AFTER, --after AFTER
                        Commits after/since date
  -u BEFORE, --before BEFORE
                        Commits before/until date
  -k, --keeptemp        Keep any created temp files (Default: false)

```

## Custom editor
The default editor is less (remember, less is more), but that can be changed.
```
$ viewlog <filename> --editor [vi|vim|mvim|gvim|more|emacs]
```
As of version 1.1.4, the operating system emacs is supported.

You can also open binary files. For instance on a mac to open a animated gif, I do:
```
$ viewlog viewlog.gif --editor "open -a Safari"
```

## Custom log line
```
$ viewlog README.md --logformat "%h - %ad, %an: %s"
 => b2f88c8 - Sun Jan 24 15:21:57 2016 -0500, roubles: emacs ftw!
    d443a7c - Sun Jan 24 15:19:59 2016 -0500, roubles: vim ftw!
    cb47e52 - Sun Jan 24 15:17:26 2016 -0500, roubles: Will it blend?
    750b153 - Sun Jan 24 15:16:06 2016 -0500, roubles: All your base are belong to us.
    1e283cf - Sun Jan 24 00:58:41 2016 -0500, roubles: Update README.md
    8bba27e - Sun Jan 24 00:57:52 2016 -0500, roubles: Update README.md
    5be85d5 - Sun Jan 24 00:55:28 2016 -0500, roubles: Update README.md
    cbf5d8e - Sun Jan 24 00:48:13 2016 -0500, roubles: Update README.md
    edaceb1 - Sun Jan 24 00:45:01 2016 -0500, roubles: Update README.md
    918166c - Sun Jan 24 00:34:54 2016 -0500, rouble: initial commit
    next page
    exit
```
