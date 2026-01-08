from agewizard import Age, ac, compare_ages

def test_validation():
    print("--- Testing Strict Validation ---")
    try:
        # Invalid month
        Age("2000-22-01")
    except ValueError as e:
        print(f"Caught expected error (22nd month): {e}")

    try:
        # Invalid day for Feb
        Age("2021-02-30")
    except ValueError as e:
        print(f"Caught expected error (Feb 30): {e}")

def test_formats():
    print("\n--- Testing Custom Formats ---")
    # UK format
    uk_user = Age("31-12-1990", date_format="DD-MM-YYYY")
    print(f"UK Format (31-12-1990) -> {uk_user.years} years")

    # US format (manual override)
    us_user = Age("12.31.1990", date_format="MM.DD.YYYY")
    print(f"US Format (12.31.1990) -> {us_user.years} years")

    # Automatic detection (DD-MM-YYYY)
    auto_user = Age("15/05/1995")
    print(f"Auto-detected DD-MM-YYYY (15/05/1995) -> {auto_user.years} years")

def test_helpers():
    print("\n--- Testing Convenience Helpers ---")
    teen = Age("2010-01-01")
    adult = Age("1990-01-01")
    
    print(f"Teen (2010): is_adult? {teen.is_adult()}")
    print(f"Adult (1990): is_adult? {adult.is_adult()}")
    print(f"Adult (1990): is_adult(21)? {adult.is_adult(21)}")

if __name__ == "__main__":
    test_validation()
    test_formats()
    test_helpers()
