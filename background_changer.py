#!/usr/bin/python3.10
import datetime as dt
import glob
import os
from pathlib import Path


class BackgroundChanger:
    def __init__(self):
        self.background_images_directory = \
            Path('/home/kyle/Pictures/desktop_backgrounds')
        self.set_dbus()

    @staticmethod
    def set_dbus():
        os.environ["DBUS_SESSION_BUS_ADDRESS"] = 'unix:path=/run/user/1000/bus'

    def _get_background_image_paths(self):
        p = self.background_images_directory.joinpath('*')
        return sorted(glob.glob(str(p)))

    def _get_daily_image_filename(self):
        images = self._get_background_image_paths()
        weekday_number = dt.datetime.today().weekday()
        return images[weekday_number]

    def change_background(self):
        daily_picture_filename = self._get_daily_image_filename()
        self._set_wallpaper(daily_picture_filename)

    @staticmethod
    def _set_wallpaper(image):
        cmd = f'gsettings set org.gnome.desktop.background picture-uri {image}'
        os.system(cmd)
        print(f'Successfully changed wallpaper at {dt.datetime.now()}')


if __name__ == '__main__':
    # This works as long as you have at least 7 pictures in a folder
    # Then add '0 0 * * * /path/to/python3 /path/to/script.py' to cron to
    # change it at midnight every day
    n = BackgroundChanger()
    n.change_background()
