# Stack is a LIFO (Last in first out) data structure
# The last added element is taken the first
# Time complexity is O(1) for both removal and addition

my_stack = []

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)

print(f"The top element: {my_stack[-1]}")

while my_stack:
    print(my_stack.pop())