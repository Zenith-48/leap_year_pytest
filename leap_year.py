def leap(num):
    return (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        if leap(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print("Usage: python leap.py <year>")
