def my_function(x):
    if x == 0:
        return 0
    else:
        return 1 / x

result = my_function(0)
print(result) # Output: 0

#Alternative solution:

def my_function(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 0

result = my_function(0)
print(result) # Output: 0