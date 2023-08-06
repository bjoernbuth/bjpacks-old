# bjpacks

This is mainly a repo to test building python packages.
It is intended for maintaining scripts I write for myself
to make things easier (of course everyone is willcome to use
these scripts). 

The scripts for directory bookmarks are inspired by awesome bashmarks
utility you can find here: (https://github.com/huyng/bashmarks)[https://github.com/huyng/bashmarks]

At first I made similar scripts in python that were separated to:
- savedir.py (aliased to sav or even s via doskey)
- list_saved_dir.py (aliased to lis or even l via doskey)
- goto_saved_dir.py (aliased to gts or g)

However since windows cmd lacks a shebang it was neccessary to create
wrapper bat scripts (savedir.bat etc) to call the python scripts. 

Once the number of personal tools increases this becomes time consuming 
and even for single scripts is quite annoying. 

That's why I switched to putting my tools into a packagage that 
I simply install via:

```
pip install .
```

To be able to directly use the scripts the user scripts in the (user)
python dir have to be in the path (the above command will install as user 
since I don't work as admin unless I have to). 
