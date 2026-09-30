# ---------------------------------------
# Code Explanation Prompt
# ---------------------------------------

CODE_EXPLANATION_PROMPT = """
You are an expert {language} programming instructor.

Explain the following code line by line.

For every line include:

• Purpose
• Logic
• Syntax
• Example if needed

Code:

{code}
"""

# ---------------------------------------
# Code Review Prompt
# ---------------------------------------

CODE_REVIEW_PROMPT = """
You are an experienced software engineer.

Review the following {language} code.

Provide:

1. Bugs
2. Performance Improvements
3. Readability Suggestions
4. Security Issues
5. Best Practices

Code:

{code}
"""

# ---------------------------------------
# Complexity Analysis Prompt
# ---------------------------------------

COMPLEXITY_PROMPT = """
Analyze this {language} code.

Return:

Time Complexity

Space Complexity

Explain why.

Code:

{code}
"""

# ---------------------------------------
# Optimizer Prompt
# ---------------------------------------

OPTIMIZER_PROMPT = """
Optimize the following {language} code.

Requirements:

• Make it shorter
• Improve readability
• Improve performance
• Follow best practices

Return the optimized code first.

Then explain the improvements.

Code:

{code}
"""

# ---------------------------------------
# Beginner Explanation Prompt
# ---------------------------------------

BEGINNER_PROMPT = """
Explain this {language} code as if teaching a beginner.

Avoid technical jargon.

Use simple language.

Use real-life analogies whenever possible.

Code:

{code}
"""

# ---------------------------------------
# Bug Detection Prompt
# ---------------------------------------

BUG_PROMPT = """
Find bugs in the following {language} code.

Return:

• Syntax Errors
• Logical Errors
• Runtime Errors
• Possible Fixes

Code:

{code}
"""

# ---------------------------------------
# RAG Prompt
# ---------------------------------------

RAG_PROMPT = """
You are an expert programming assistant.

Answer the user's question using ONLY the provided documentation.

If the answer is not available in the documentation,
say that the information was not found.

Documentation:

{context}

Question:

{question}
"""