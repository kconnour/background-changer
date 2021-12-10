background-changer
==================
This code programatically changes the desktop backgrounds to user-defined
images. This only works on Gnome-based operating systems. I couldn't find a
program that did this so I made my own.

Setup
-----
Start by cloning the repo and opening `background_changer.py`. Change the
`background_images` variable to the path of the folder containing images you'd
like to cycle through. Also note that I set the dbus address in the
constructor and I don't think this changes between distros, but I'm not
positive.

Then open cron in Terminal with `crontab -e` and set the times when you'd like
this code to cycle through backgrounds. You can either set your Python
interpreter here or simply shebang `background_changer.py`. For example, I
change my background everyday at midnight with this command:
`0 0 * * * /usr/bin/python3.10 /home/kyle/repos/background-changer/background_changer.py`.
If you get any errors you can also capture the error by appending
`> /home/kyle/.cron_stdout_background.txt 2>&1` to that command.

As long as the required number of images are in the directory you set you
should be all set!
