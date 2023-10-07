import ast

def find_undefined_functions(code):
    # Parse the Python code
    tree = ast.parse(code)
    
    # Collect all defined function names
    defined_functions = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defined_functions.add(node.name)
    
    # Collect all function calls
    function_calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            function_calls.add(node.func.id)
    
    # Find undefined functions
    undefined_functions = function_calls - defined_functions
    print(undefined_functions)
    return undefined_functions

