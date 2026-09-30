import ast


def analyze_python_code(code: str):

    tree = ast.parse(code)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):

            for module in node.names:
                imports.append(module.name)

        elif isinstance(node, ast.ImportFrom):

            module = node.module

            if module:
                imports.append(module)

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports
    }