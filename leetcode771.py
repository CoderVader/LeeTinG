def numJewelsInStones(J, S):
    return sum(map(J.count, S))

# def numJewelsInStones(J, S):
#     return sum(s in J for s in S)

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("zz", "ZZxert"))
print(numJewelsInStones("bcd", "ABcEFd"))