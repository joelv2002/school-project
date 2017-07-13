def fibonacci(n):
    x = range(0,n)
    end = []
    for i in range (0,n):
        if i == 0:
            end.append(x[1]+x[0])
        else:
            end.append(x[i]+x[i-1])
    return end
print(fibonacci(6))
