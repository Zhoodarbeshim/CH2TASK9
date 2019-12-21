# n = int(input())

# factorial = 1
# while n > 1:
#     factorial *=n
#     n -= 1
# print(factorial)

n = int(input())
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(factorial)