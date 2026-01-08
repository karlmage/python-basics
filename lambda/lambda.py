# Basic syntax
x = lambda a, b, c: a + b + c
print(x(1, 3, 2))

# Wrapping lambda
def lambda_wrapper(n):
    return lambda a: a * n

end_function = lambda_wrapper(2) # Creates a lambda function instance
print(end_function(6)) # Executes the lambda function instance and prints the result
