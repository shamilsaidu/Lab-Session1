import lab1_ml as lab1

list_1 = [2, 7, 4, 1, 3, 6]
print("the number of pairs that add upto 10 are :",lab1.q1(list_1))

list_2 = [5, 3, 8, 1, 0, 4]
# list_2 = [0]
print(lab1.q2(list_2))

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = 5
print(lab1.q3(matrix_1, m1))

input_string_4 = "hippopotamus"
result_4 = lab1.q4(input_string_4)
print(f"Question 4: Highest occurring character is '{result_4[0]}' with occurrence count {result_4[1]}")
