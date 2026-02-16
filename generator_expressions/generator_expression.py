result = sum(i for i in range(5))
print(result)

result = sum(i*i for i in range(5))
print(result)

line = "Today I I  will will cook bread bread with eggs eggs"
unique_words = set(word for word in line.split())
print(unique_words)

xvec = [4, 5, 10]
yvec = [6, 7, 8]
result = sum(x*y for x, y in zip(xvec, yvec))
print(result)

data = "butIamacreep"
result = list(data[i] for i in range(len(data) - 1, -1, -1))
print(result)

