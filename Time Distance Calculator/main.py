import datetime as dt


def main():
    try:
        current = dt.datetime.now()
        target = input("Enter date (ex. YYYY-MM-DD): ")
        target_year, target_month, target_day = map(int, target.split("-"))
        target_time = dt.datetime(target_year, target_month, target_day)
        diff = target_time - current

        day, seconds = diff.days, diff.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        if diff.total_seconds() < 0:
            print("Date is in the past.")
        else:
            print(f"Count Down: {day} days, {hours} hours, {minutes} minutes, and {seconds} seconds")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


if __name__ == "__main__":
    main()
