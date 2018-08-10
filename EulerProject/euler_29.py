def get_result():
    results = []
    for a in range(100,1,-1):
        for b in range(2,101):
            res = a**b
            if res not in results:
                results.append(res)
    return len(results)