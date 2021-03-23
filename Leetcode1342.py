def numberOfSteps(num):
    step = 0
    result = num
    # print(result)
    while result > 0:
        if result % 2 == 0:
            result = result // 2
            step += 1
            # print(result)
        else:
            result -= 1
            step += 1
            # print(result)
    return step


