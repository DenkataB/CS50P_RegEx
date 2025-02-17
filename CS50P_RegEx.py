import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"(\d{1,2})(:\d{2})?\s(AM|PM)\sto\s(\d{1,2})(:\d{2})?\s(AM|PM)", s)

    if not matches:
        raise ValueError

    first_hour = convert_24h(matches.group(1), matches.group(3))
    second_hour = convert_24h(matches.group(4), matches.group(6))

    if matches.group(2):
        first_minutes = matches.group(2)
    else:
        first_minutes = ":00"

    if matches.group(5):
        second_minutes = matches.group(5)
    else:
        second_minutes = ":00"

    if int(first_minutes.lstrip(":")) < 60 and int(second_minutes.lstrip(":")) < 60:
        return f"{first_hour}{first_minutes} to {second_hour}{second_minutes}"
    else:
        raise ValueError

def convert_24h(hour, period):
    hour = int(hour)
    if period == "PM" and hour < 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}"

if __name__ == "__main__":
    main()
