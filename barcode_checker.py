# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   11.15 LAB: Barcode checker
# Date:         2 November 2025

def barcode_validity_checker(barcode):
    first_group = [int(barcode[0]), int(barcode[2]), int(barcode[4]), int(barcode[6]), int(barcode[8]), int(barcode[10])]
    second_group = [int(barcode[1]), int(barcode[3]), int(barcode[5]), int(barcode[7]), int(barcode[9]), int(barcode[11])]
    if str(10 - ((3*sum(second_group) + sum(first_group)) % 10)) == barcode[12]:
        return True
    else:
        return False

def main():
    user_input_file_name = input("Enter the name of the file: ")
    valid_barcodes_counter = 0
    with open(user_input_file_name, "r") as user_input_file, open("valid_barcodes.txt", "w") as valid_barcodes_file:
        for line in user_input_file:
            barcode = line.strip()
            barcode_validity = barcode_validity_checker(barcode)
            if barcode_validity == True:
                valid_barcodes_counter += 1
                valid_barcodes_file.write(f"{barcode}\n")
    print(f"There are {valid_barcodes_counter} valid barcodes")

# Maximus was here :)
if __name__ == '__main__':
    main()