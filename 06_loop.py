i=1
while i<=5:
    print(i * "*")
    i+=1


# *
# **
# ***
# ****
# *****

# i + "*" throw error because you are trying to concat string here


# 0 ->  <2
for i in range(2):
    print(f"Iteration number: {i}")

# Iteration number: 0
# Iteration number: 1

# range(start, stop, step)
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i, end=" ")

print()
for i in range(5, 0, -1):  # 5 to 1
    print(i, end=" ")
