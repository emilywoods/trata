import time

from rich.console import Console
from rich.table import Table

GREETING_MORNING = "Good morning! :sunrise:"
GREETING_AFTERNOON = "Good afternoon :wave:"
GREETING_EVENING = "Good evening :city_sunrise:"
GREETING_NIGHTIME = "Hello, Nightowl :owl:"


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
Today we will do pomodoros for [b]25 minutes[/b]. \n
There will be [b] short 5 minute breaks [/b]in between each pomodoro.\n
After 4x pomodoros, there will be a [b]long break of 15 minutes[/b].\n
:tomato: 
"""
    )

    console.print(table)


def main():
    console = Console()
    greeting_table(console)


if __name__ == "__main__":
    main()
