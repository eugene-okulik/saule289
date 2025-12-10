import datetime
import os


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "..", "..", "eugene_okulik", "hw_13", "data.txt")
file_path = os.path.abspath(file_path)
now = datetime.datetime.now()
print(file_path)


def extract_date(line):
    line = line.strip()
    number, date = line.split(".", 1)
    date_total, action = date.split(" - ", 1)
    date_total = date.strip()
    date_from_file = datetime.datetime.strptime(date_total, "%Y-%m-%d %H:%M:%S.%f")

    if "на неделю" in action:
        new_date = date_from_file + datetime.timedelta(weeks=1)
        print(new_date)
    elif "какой это будет день недели" in action:
        weekday = date_from_file.strftime("%A")
        print(weekday)
    elif "сколько дней назад была эта дата" in action:
        diff = now - date_from_file
        print(diff.days)


def read_file():
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                extract_date()
