from backend.report.pdf_generator import generate_pdf

file = generate_pdf(
    language="Python",
    code="print('Hello World')",
    explanation="Prints Hello World.",
    review="Good code.",
    bugs="No bugs found.",
    optimization="Already optimized.",
    complexity="O(1)"
)

print(file)