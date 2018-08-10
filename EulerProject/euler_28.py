def spiral_sum(size):
    grid = int(size/2)
    num = 1
    total = 1
    step = 1
    for i in range(grid):
        for l in range(4):
            num += step+1
            total += num
        step += 2
    return total

def get_result(size):
    return spiral_sum(size)