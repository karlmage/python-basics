# Queue is a LILO (Last in last out) data structure
# The last added element is being accessed the last
# Linked lists are usually used to implement these

from collections import deque

my_queue = deque()

# Enque
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.append(4)
my_queue.append(5)

# Deque
while my_queue:
    print(my_queue.popleft())


