def triangles(limit=None, t_limit=None):
    control, triangle = 0, 0
    while True:
        if limit and control > limit:
            break
        if t_limit and triangle > t_limit:
            break
        control += 1
        triangle += control
        yield triangle