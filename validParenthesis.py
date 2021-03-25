def isBalance(s):

    # initializing the stack
    stack = []
    brackets = {'{': '}', '(': ')', '[': ']'}

    # traverse through the string
    for char in s:
        # if we find an opening bracket then we push it into the stack
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            # If stack is not empty
            if stack:
                # Pop the top element
                top = stack.pop()

                # Compare with the found closing bracket
                if brackets[top] != char:
                    return "NO"

            else:
                return "NO"

    if stack:
        return "NO"
    return "Yes"
    # return "NO" if stack else "YES"


