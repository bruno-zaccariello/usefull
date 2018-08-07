def triangles(limit=None):
    control, triangle = 0, 0
    while True:
        if limit and control > limit:
            break
        control += 1
        triangle += control
        yield triangle