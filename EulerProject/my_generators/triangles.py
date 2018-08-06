def triangles(limit=None):
    control, triangle = 0, 0
    while True and control < limit:
        control += 1
        triangle += control
        yield triangle