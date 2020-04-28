# Multiples of 3 and 5
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# I like this Solution
def sum_of_all_the_multiples(Max_Number, div_a_Number, div_b_Number):
    return sum(set(list(range(0, Max_Number, div_a_Number)) + list(range(0, Max_Number, div_b_Number))))
print(sum_of_all_the_multiples(1000, 3, 5))


# Use this Solution if you need Cycle
Max_Number, div_a_Number, div_b_Number = 1000, 3, 5
result = 0
for i in range(0, Max_Number):
    if i % div_a_Number == 0 or i % div_b_Number == 0:
        result += i
print(result)
