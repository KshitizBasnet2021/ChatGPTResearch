#shunting_yard.py
#
#There is a bug in the provided code. The code does not handle the case when the token is an operator and the operator stack is empty. This can result in an IndexError when trying to access `opstack[-1]` in the line `while opstack and precedence[token] <= precedence[opstack[-1]]:`.
#
#To fix this bug, you can add a check to ensure that the operator stack is not empty before accessing `opstack[-1]`. Here's the modified code:
#
#```python
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
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
#
    while opstack:
        rpntokens.append(opstack.pop())
#
    return rpntokens
#```
#
#This fix ensures that the operator stack is not empty before accessing `opstack[-1]`, preventing the IndexError.
#
#
#