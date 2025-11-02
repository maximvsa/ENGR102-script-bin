# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   11.10 LAB: Passport checker Part B
# Date:         2 November 2025

import re

def valid_value(passport):
    if "iyr" not in passport or "eyr" not in passport or "hgt" not in passport or "hcl" not in passport or "ecl" not in passport or "pid" not in passport or "cid" not in passport:
        return False
    if not re.fullmatch(r"\d{4}", passport["iyr"]):
        return False
    if not (2015 <= int(passport["iyr"]) <= 2025):
        return False
    if not re.fullmatch(r"\d{4}", passport["eyr"]):
        return False
    if not (2025 <= int(passport["eyr"]) <= 2035):
        return False
    m = re.fullmatch(r"(\d+)(cm|in)", passport["hgt"])
    if not m:
        return False
    n, u = int(m.group(1)), m.group(2)
    if u == "cm" and not (150 <= n <= 193):
        return False
    if u == "in" and not (59 <= n <= 76):
        return False
    if not re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"]):
        return False
    if passport["ecl"] not in {"amb","blu","brn","gry","grn","hzl","oth"}:
        return False
    if not re.fullmatch(r"\d{9}", passport["pid"]):
        return False
    if not re.fullmatch(r"[1-9]\d{2}", passport["cid"]):
        return False
    return True

file_name = input("Enter the name of the file: ").strip()
valid_passport_count = 0

with open(file_name, "r", encoding="utf-8") as scanned_passports_file, open("valid_passports2.txt", "w", encoding="utf-8") as valid_passports_file:
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
        if valid_value(passport):
            valid_passport_count += 1
            valid_passports_raw.append(raw_passport)

    for i, raw_passport in enumerate(valid_passports_raw):
        valid_passports_file.write(raw_passport)
        if i < len(valid_passports_raw) - 1:
            valid_passports_file.write("\n\n")

# Maximus was here :)
print(f"There are {valid_passport_count} valid passports")
