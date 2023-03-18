#!/usr/bin/python3.10
import datetime as dt
import os
from pathlib import Path


def get_seasonal_folder():
    current_day_of_year = dt.date.today().timetuple().tm_yday
    day_of_year_boundaries = (
        dt.date(2022, 1, 1).timetuple().tm_yday,
        dt.date(2022, 3, 21).timetuple().tm_yday,
        dt.date(2022, 6, 21).timetuple().tm_yday,
        dt.date(2022, 9, 21).timetuple().tm_yday,
        dt.date(2022, 10, 1).timetuple().tm_yday,
        dt.date(2022, 11, 1).timetuple().tm_yday,
        dt.date(2022, 12, 21).timetuple().tm_yday,
        dt.date(2022, 12, 31).timetuple().tm_yday + 1,
    )
    folders = (
        'winter',
        'spring',
        'summer',
        'fall',
        'halloween',
        'fall',
        'winter'
    )
    for day in range(len(day_of_year_boundaries)-1):
        if day_of_year_boundaries[day] <= current_day_of_year < day_of_year_boundaries[day+1]:
            return folders[day]


def change_background(img_dir: Path, dark_mode=True):
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = 'unix:path=/run/user/1000/bus'
    image_location = img_dir / get_seasonal_folder()
    image_paths = sorted(image_location.glob('*'))
    weekday_number = dt.datetime.today().weekday()  # 0 is Monday
    daily_filepath = image_paths[weekday_number]

    print(daily_filepath)

    # This was added in Ubuntu 22.04 with Wayland. Previous Ubuntus don't have the dark mode as an option
    key = '-dark' if dark_mode else ''
    os.system(f'gsettings set org.gnome.desktop.background picture-uri{key} {daily_filepath}')
    print(f'Successfully changed wallpaper at {dt.datetime.now()}')


if __name__ == '__main__':
    # This works as long as you have at least 7 pictures in a folder
    # Then add '0 0 * * * /path/to/python3 /path/to/script.py' to cron to
    # change it at midnight every day

    pictures = Path('/home/kyle/Pictures/desktop-backgrounds/')
    change_background(pictures)
