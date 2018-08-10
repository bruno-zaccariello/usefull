def get_result():
    result = []
    for i in range(2,531441):
        digits = str(i)
        total = sum(int(x)**5 for x in digits)
        if total == i:
            result.append(i)
    return result