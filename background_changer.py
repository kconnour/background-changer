#!/usr/bin/python3.10
import datetime as dt
import os
from pathlib import Path


def change_background(img_dir: str, dark_mode=True):
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = 'unix:path=/run/user/1000/bus'
    image_paths = sorted(Path(img_dir).glob('*'))
    weekday_number = dt.datetime.today().weekday()  # 0 is Monday
    daily_filepath = image_paths[weekday_number]

    # This was added in Ubuntu 22.04 with Wayland. Previous Ubuntus don't have the dark mode as an option
    key = '-dark' if dark_mode else ''
    os.system(f'gsettings set org.gnome.desktop.background picture-uri{key} {daily_filepath}')
    print(f'Successfully changed wallpaper at {dt.datetime.now()}')


if __name__ == '__main__':
    # This works as long as you have at least 7 pictures in a folder
    # Then add '0 0 * * * /path/to/python3 /path/to/script.py' to cron to
    # change it at midnight every day

    spring = '/home/kyle/Pictures/desktop_backgrounds/spring'
    change_background(spring)
