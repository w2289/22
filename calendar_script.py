import argparse
import calendar
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Print a monthly calendar")
    parser.add_argument("year", nargs="?", type=int, help="Year of the calendar", default=datetime.now().year)
    parser.add_argument("month", nargs="?", type=int, help="Month of the calendar (1-12)", default=datetime.now().month)
    args = parser.parse_args()

    if not 1 <= args.month <= 12:
        parser.error("month must be in 1..12")
    cal = calendar.TextCalendar()
    print(cal.formatmonth(args.year, args.month))


if __name__ == "__main__":
    main()
