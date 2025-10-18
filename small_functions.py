# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   9.20 LAB: Small functions
# Date:         18 October 2025

def parta(num_list):
    # yeah yeah, Maximus imported from statistics; Settle down!
    import statistics
    return min(num_list), statistics.median(num_list), max(num_list)

def partb(time_list, distances_list):
    # dD/dt -> basic calculus (slope formula)
    rates = []
    for i in range(len(time_list) - 1):
        delta_t = time_list[i + 1] - time_list[i]
        rates.append((distances_list[i + 1] - distances_list[i]) / delta_t)
    return rates

def partc(num_list):
    # Pretty straightforward
    for i in num_list:
        for k in num_list:
            if i + k == 2029:
                return i*k
    return False

def partd(n):
    # This one is weird; I already forgot how it works ngl
    if n <= 0:
        return False
    for i in range(2, n, 2):
        total = 0
        sequence = []
        j = i
        while total < n:
            sequence.append(j)
            total += j
            if total == n:
                if len(sequence) >= 2:
                    return sequence
                break
            j += 2
    return False

def parte(r_s, r_h):
    import math
    # Formula for volume of a spherical bead in terms of radius of sphere and radius of hole
    return (4/3) * math.pi * (r_s**2 - r_h**2)**(3/2)

def partf(char, name, company, email):
    # Now, this one is pretty cool ngl
    horizontal_border = char * (max([len(name), len(company), len(email)]) + 6)
    name_line = char + name.center(max([len(name), len(company), len(email)]) + 4) + char
    company_line = char + company.center(max([len(name), len(company), len(email)]) + 4) + char
    email_line = char + email.center(max([len(name), len(company), len(email)]) + 4) + char
    return horizontal_border + "\n" + name_line + "\n" + company_line + "\n" + email_line + "\n" + horizontal_border

def partg(x, tolerance):
    # Borrowed from approximating_ln.py lol
    approximation = 0
    for n in range(1, 999999):
        next_term = (2/(2*n - 1)) * x**(2*n - 1)
        if abs(next_term) < tolerance:
            break
        approximation += next_term
    return approximation