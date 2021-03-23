def kidsWithCandies(candies, extraCandies):
    max_kid = max(candies)
    l = []
    for i in range(0, len(candies)):
        if candies[i] + extraCandies >= max_kid:
            l.append("true")
        else:
            l.append("false")
    return l

# TestCases

assert kidsWithCandies([2,3,5,2,1],3) == ['true', 'true', 'true', 'true', 'false']
assert kidsWithCandies([10,13,9,7,11],3) == ['true', 'true', 'false', 'false', 'true']
assert kidsWithCandies([7,3,4],2) == ['true', 'false', 'false']
