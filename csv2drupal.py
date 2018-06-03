
import sys
import csv

if __name__ == "__main__":
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)