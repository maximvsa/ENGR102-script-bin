import string
import numpy as np

data_file = "module12quizF25.txt"
hidden_message = "tcgscufpxiz"

values = np.loadtxt(data_file, dtype=int)
matrix = values.reshape(100, 100)

n1 = np.mean(matrix[5])
n2 = np.min(matrix[:][28])
n3 = np.max([matrix[i][23] for i in range(3)])
n4 = np.sum([matrix[99][-i] for i in range(1, 4)])
n5 = np.min([matrix[90][-i] for i in range(1, 4)])

number_to_letter = lambda number: chr(ord("a")+int(number))

code_letters = [number_to_letter(i) for i in [n1, n2, n3, n4, n5]]
code_string = ''.join(code_letters)

print(f'The word is "{code_string}"')

cipherbet = code_letters + [letter for letter in string.ascii_lowercase[(n5):] if letter not in code_letters] + ["b"]

print("".join(cipherbet))