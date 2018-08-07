def get_result():
    total = str(2**1000)
    total_list = list(int(x) for x in total)
    return sum(total_list)