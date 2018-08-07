def get_result():
    max = [0]
    for n in range(0,10**6):
        max_num = n
        operations = 0
        while n > 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = (3*n) + 1
            operations += 1
        if operations > max[0]:
            max = operations, max_num
    return max