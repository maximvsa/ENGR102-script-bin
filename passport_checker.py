# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   11.9 LAB: Passport checker Part A
# Date:         2 November 2025

def passport_validity_checker(passport):
    required_attributes = ["iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for field in required_attributes:
        if field not in passport:
            return False
    return True

file_name = input("Enter the name of the file: ").strip()
valid_passport_count = 0

with open(file_name, "r", encoding="utf-8") as scanned_passports_file, open("valid_passports.txt", "w", encoding="utf-8") as valid_passports_file:
    file_contents = scanned_passports_file.read()
    scanned_passports = [p for p in file_contents.split("\n\n") if p.strip()]
    valid_passports_raw = []

    for raw_passport in scanned_passports:
        fields = raw_passport.replace("\n", " ").strip().split()
        passport = {}
        for field in fields:
            if ":" in field:
                k, v = field.split(":", 1)
                passport[k] = v
        if passport_validity_checker(passport):
            valid_passport_count += 1
            valid_passports_raw.append(raw_passport)

    for i, raw_passport in enumerate(valid_passports_raw):
        valid_passports_file.write(raw_passport)
        if i < len(valid_passports_raw) - 1:
            valid_passports_file.write("\n\n")

# Comment
print(f"There are {valid_passport_count} valid passports")
