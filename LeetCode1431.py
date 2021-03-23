def kidsWithCandies(candies, extraCandies):
    max_kid = max(candies)
    l = []
    for i in range(0, len(candies)):
        if candies[i] + extraCandies >= max_kid:
            l.append("true")
        else:
            l.append("false")
    return l

k = kidsWithCandies([2,3,5,2,1],3)
print(k)