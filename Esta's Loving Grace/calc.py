for increments in range(360):
    result = 0
    steps = 0
    x = 1
    while x:
        steps += 1
        result += increments
        x = result % 360
    print(f"Increments {increments} : Steps {steps} : Final heading {result}")


