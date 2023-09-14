#../python_programs/shunting_yard.py
#
#Yes, there is a bug in the provided code. The bug is in the while loop where the operator stack is being checked. The condition `precedence[token] <= precedence[opstack[-1]]` should be `precedence[token] < precedence[opstack[-1]]` to ensure that operators with equal precedence are not popped from the stack prematurely.
#
#Here is the fixed code:
#
def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
#
    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        else:
            while opstack and precedence[token] < precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
#
    while opstack:
        rpntokens.append(opstack.pop())
#
    return rpntokens
#
#Now the code should work correctly and convert infix notation to Reverse Polish Notation (RPN) properly.
#
#
#