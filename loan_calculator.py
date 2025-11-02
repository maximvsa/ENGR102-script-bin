# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   11.16 LAB: Loan calculator
# Date:         2 November 2025

def monthly_payment_calculator(P, N, i):
    monthly_payment = (P * i / 12) / (1 - (1 / (1 + i / 12)) ** N)
    return monthly_payment

def total_accrued_interest_calculator(principal_amount, annual_rate, term_length, months_elapsed):
    if months_elapsed <= 0:
        return 0
    
    capped_months = min(months_elapsed, term_length)
    
    if annual_rate == 0:
        return 0
    
    monthly_rate = annual_rate / 12
    payment = monthly_payment_calculator(principal_amount, term_length, annual_rate)
    growth_factor = (1 + monthly_rate) ** capped_months
    remaining_balance = principal_amount * growth_factor - payment * (growth_factor - 1) / monthly_rate
    
    accrued_interest = payment * capped_months - principal_amount + remaining_balance
    return max(accrued_interest, 0)

def loan_balance_calculator(principal_amount, annual_rate, term_length, months_elapsed):
    if months_elapsed <= 0:
        return float(principal_amount)
    
    capped_months = min(months_elapsed, term_length)
    
    if annual_rate == 0:
        payment = principal_amount / term_length
        remaining = principal_amount - payment * capped_months
        return max(remaining, 0)
    
    monthly_rate = annual_rate / 12
    payment = monthly_payment_calculator(principal_amount, term_length, annual_rate)
    growth_factor = (1 + monthly_rate) ** capped_months
    remaining_balance = principal_amount * growth_factor - payment * (growth_factor - 1) / monthly_rate
    return max(remaining_balance, 0)

def main():
    user_input_output_filename = input("Enter the output filename: ")
    user_input_principal_amount = input("Enter the principal amount: ")
    user_input_term_length = input("Enter the term length (months): ")
    user_input_annual_interest_rate = input("Enter the annual interest rate: ")
    
    term_length = int(user_input_term_length)
    principal_amount = float(user_input_principal_amount)
    annual_interest_rate = float(user_input_annual_interest_rate)
    
    with open(user_input_output_filename, "w") as output_file:
        output_file.write("Month,Total Accrued Interest,Loan Balance\n")
        output_file.write(f"0,$0.00,${principal_amount:.2f}\n")
        
        
        for month in range(1, term_length + 1):
            total_accrued_interest = total_accrued_interest_calculator(principal_amount, annual_interest_rate, term_length, month)
            loan_balance = loan_balance_calculator(principal_amount, annual_interest_rate, term_length, month)
            
            output_file.write(f"{month},${total_accrued_interest:.2f},${loan_balance:.2f}\n")

# Maximus was here :)
if __name__ == "__main__":
    main()