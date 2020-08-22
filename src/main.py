import sys
import time

from rich.console import Console
from rich.progress import track
from rich.table import Table

GREETING_MORNING = ":sunrise: Good morning! :sunrise:"
GREETING_AFTERNOON = "Good afternoon :wave:"
GREETING_EVENING = ":city_sunset: Good evening! :city_sunset:"
GREETING_NIGHTIME = ":milky_way: Hello, Nightowl :owl:"


def current_hour() -> str:
    return time.localtime().tm_hour


def greeting() -> str:
    hour = current_hour()

    if 5 < hour < 12:
        return GREETING_MORNING
    elif 12 < hour < 17:
        return GREETING_AFTERNOON
    elif 17 < hour < 23:
        return GREETING_EVENING
    else:
        return GREETING_NIGHTIME


def greeting_table(console: Console):
    table = Table(show_header=True, header_style="bold green")
    table.add_column(greeting(), style="dim", justify="center")
    table.add_row(
        """
Today we'll do Pomodoros for [b]25 minutes[/b]. \n
There will be [b]short 5 minute breaks [/b]in between each one.\n
After 4x Pomodoros, there will be a [b]long break of 15 minutes[/b].\n
:tomato: 
"""
    )

    console.print(table)


def countdown_to_begin(console: Console):
    console.print("Starting in:")
    seconds_until_start = 5
    while seconds_until_start > 0:
        console.print(f"{seconds_until_start}")
        seconds_until_start = seconds_until_start - 1
        time.sleep(1)


def run_pomodoros(console: Console):
    pomo_in_sec = 25 * 60
    for n in track(
        range(pomo_in_sec), description="[cyan]Pomodoro 1[/cyan] :: In progress"
    ):
        time.sleep(1)
    sys.stdout.write("\a")


def main():
    console = Console()

    greeting_table(console)
    begin = input("Begin pomodoro session? y/n ")
    if begin is "y":
        countdown_to_begin(console)
        run_pomodoros(console)
    else:
        exit()


if __name__ == "__main__":
    main()
