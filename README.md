# Usage

+ Create a shortcut of Sticky Notes(you can find the executable program in the start menu, then pull it to the desktop)
+ Fill in the 'USERNAME' and 'lnk_path' in 'main.py' with your Windows username and the shortcut path
+ Run 'setup.exe' and follow its tip.

# Q & A

1. Why don't you use 'stikynot.exe' command in os.system() to execute StickyNotes?  
   I have tried this way, but it didn't work. It appears that Windows 10 doesn't support this command any more.

2. Why the final step has to be done by user?  
   Well, moving an app to the Startup directory needs Superuser, but I haven't found a way to do that automatically.
