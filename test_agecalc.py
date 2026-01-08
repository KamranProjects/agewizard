from agecalc import Age, compare_ages
from datetime import date

def test_full_features():
    dob = "2000-01-01"
    person = Age(dob)
    
    print(f"--- Testing Agecalc for DOB: {dob} ---")
    print(f"Years: {person.years}")
    print(f"Months: {person.months}")
    print(f"Weeks: {person.weeks}")
    print(f"Days: {person.days}")
    print(f"Zodiac: {person.zodiac}")
    print(f"Leap Year: {person.leap_year}")
    print(f"Next Birthday in: {person.next_birthday_days} days")
    print(f"Next Birthday Weekday: {person.next_birthday_weekday}")
    print(f"Human Readable: {person.readable}")
    print(f"Category: {person.category}")
    print(f"Is Birthday Today? {person.is_today}")
    print(f"Hijri Age (Approx): {person.hijri_age}")
    
    print("\n--- Testing Comparison ---")
    dob2 = "1995-05-15"
    print(compare_ages(dob, dob2))

    print("\n--- Testing Birthday Message ---")
    today = date.today().strftime("%Y-%m-%d")
    today_age = Age(today)
    if today_age.is_today:
        print(f"Happy Birthday! (DOB: {today})")

if __name__ == "__main__":
    test_full_features()
