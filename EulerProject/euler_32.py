from my_functions.my_math import get_divisors

def get_result():
    results = []
    order = [1,2,3,4,5,6,7,8,9]
    order_len = len(order)
    for i in range(1000,99999):
        match = []
        divs = get_divisors(i)
        if len(divs) % 2 == 0:
            for d in range(0,len(divs)-1,2):
                test = list(int(x) for x in (str(i) + str(divs[d]) + str(divs[d+1])) )
                if len(test) != order_len:
                    continue
                else:
                    test.sort()
                    if test == order:
                        results.append(i)
                        break
    return sum(results)