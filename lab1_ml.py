def q1(input_list):
    count = 0  # initialize the count variable
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)): # using 2 nested for loops to find the pairs of numbers that add upto 10
            if input_list[i] + input_list[j] == 10:
                count += 1

    return count


def q2(input_list):
    if len(input_list) < 3:  # checking if the basic condition of having more than 3 elements are met.
        return "Range determination not possible."

    else:
        return max(input_list) - min(input_list)  # returns the required difference.


def q3(matrix, m):
    result = matrix.copy()  # initial value if the result (used if m = 1)
    for i in range(m - 1):
        result = multiply_matrix(result, matrix)  # to multiply the matrix according to the power provided using thw multiply_matrix function

    return result


def multiply_matrix(matrix1, matrix2):  # function to multiply matrices
    result = []
    for i in range(len(matrix1)):
        rows = []
        for j in range(len(matrix2[0])):
         sum = 0
         for k in range(len(matrix1[0])):
             sum += matrix1[i][k] + matrix2[k][j]

         rows.append(sum)
        result.append(rows)
    return result

def q4(input_string):
        letter_count = {}

        for letter in input_string:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1

        if not letter_count:
            return "No alphabets in the input string"

        most_frequent_letter = max(letter_count, key=letter_count.get)
        frequency_of_most_frequent_letter = letter_count[most_frequent_letter]

        return most_frequent_letter, frequency_of_most_frequent_letter

