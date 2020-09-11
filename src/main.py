import sys
import time
from time import localtime, strftime

import click
from rich.console import Console
from rich.progress import track
from rich.table import Table

GREETING_MORNING = ":sunrise: Good morning! :sunrise:"
GREETING_AFTERNOON = "Good afternoon :wave:"
GREETING_EVENING = ":city_sunset: Good evening! :city_sunset:"
GREETING_NIGHTIME = ":milky_way: :owl: Hello, Nightowl :owl: :milky_way:"


def current_hour() -> str:
    return time.localtime().tm_hour


def greeting() -> str:
    hour = current_hour()

    if 5 < hour <= 12:
        return GREETING_MORNING
    elif 12 < hour <= 16:
        return GREETING_AFTERNOON
    elif 16 < hour <= 21:
        return GREETING_EVENING
    else:
        return GREETING_NIGHTIME


def greeting_table(
    console: Console, focus_time: int, break_short_time: int, break_long_time: int
):
    table = Table(show_header=True, header_style="bold green")
    table.add_column(greeting(), style="dim", justify="center")
    table.add_row(
        f"""
Today we'll focus for [b]{focus_time} minute[/b] intervals. \n
There will be [b]short {break_short_time} minute breaks [/b]in between each focus period.\n
After 4x Pomodoros, there will be a [b]long break of {break_long_time} minutes[/b].\n
:tomato: 
"""
    )
    console.print(table)


def countdown_to_beginning(console: Console):
    console.print("Starting in:")
    seconds_until_start = 5
    while seconds_until_start > 0:
        console.print(f"{seconds_until_start}")
        seconds_until_start -= 1
        time.sleep(1)


def focus_time(time_in_min: int, cycle_num: int = 0):
    session(time_in_min, f"Pomodoro {cycle_num}")


def short_break(time_in_min: int, cycle_num: int = 0):
    session(time_in_min, f"Break {cycle_num}")


def long_break(time_in_min: int):
    session(time_in_min, ":coffee: :herb: [yellow]Long break[/yellow] :herb: :coffee:")


def session(time_in_min: int, description: str):
    start_time = strftime("%H:%M", localtime())

    for n in track(
        range(time_in_min * 60),
        description=f"[cyan]{description}[/cyan] Start time :: {start_time} ",
    ):
        time.sleep(1)
    print("\a")


@click.command()
@click.option(
    "--focus", default=25, help="Duration of time for focus, in minutes", type=click.INT
)
@click.option(
    "--break-short",
    default=5,
    help="Duration of time for short break, in minutes",
    type=click.INT,
)
@click.option(
    "--break-long",
    default=15,
    help="Duration of time for long break, in minutes",
    type=click.INT,
)
def main(focus: int, break_short: int, break_long: int):
    console = Console()

    try:

        greeting_table(console, focus, break_short, break_long)
        user_input = input("Begin pomodoro session? y/n ")
        if user_input is "y":
            countdown_to_beginning(console)

            cycle_num = 1
            while True:
                focus_time(focus, cycle_num)

                if cycle_num % 4 == 0:
                    long_break(break_long)
                else:
                    short_break(break_short, cycle_num)

                input("Click to continue with next focus period.")

                cycle_num += 1
        else:
            exit()

    except (KeyboardInterrupt, SystemExit):
        print("Exiting program. Goodbye!")


if __name__ == "__main__":
    main()
