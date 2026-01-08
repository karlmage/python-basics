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
# No imports
#
# You may use:
# map, filter
# slicing
# conditional expressions
# nested lambdas
# recursion via self-application

lambda_func = lambda a: a if len(a) in [0, 1] \
    else sum(a) if len(a)//2 == 0 \
    else ...
