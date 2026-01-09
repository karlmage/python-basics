# NESTED SIGNALS PROBLEM
# Source: ChatGPT

# Create a single Python lambda function that:
# Groups consecutive numbers by sign
# (positive, negative, or zero — zero breaks groups)
# For each group, compute:
# the sum if the group length is even
# the product if the group length is odd
# Return a list of the computed values, in order.
#
#Constraints:
# Only one lambda
# No def
# No explicit for or while
# No imports*
#
# You may use:
# map, filter, reduce*
# slicing
# conditional expressions
# nested lambdas
# recursion via self-application
#
#*Initially ChatGPT gave me this problem with both these lines
# but then removed reduce from the list when I noticed it
# had to be imported. In the end I gave up and returned the function
# back

import functools

lambda_func = lambda a: a if len(a) in [0, 1] \
                        else (list(map(lambda f: f if len(f) in [0, 1]
                                else sum(f) if len(f) % 2 == 0
                                else functools.reduce(lambda x, y: x * y, f),
                                [list(filter(lambda x: x > 0, a)),
                                list(filter(lambda x: x < 0, a)),
                                list(filter(lambda x: x == 0, a))])))

integer_list = [51, 15, -9, -8, 5, 0, 0, -15, 0, -19]
print(lambda_func(integer_list))
