import re


class CodeQualityScorer:

    def calculate(self, code: str):

        score = 100

        readability = 100
        performance = 100
        security = 100
        maintainability = 100
        documentation = 100

        suggestions = []

        # -----------------------------------
        # Empty Code
        # -----------------------------------
        if not code.strip():
            return {
                "overall": 0,
                "readability": 0,
                "performance": 0,
                "security": 0,
                "maintainability": 0,
                "documentation": 0,
                "suggestions": ["No code provided."]
            }

        lines = code.splitlines()

        # -----------------------------------
        # Long Lines
        # -----------------------------------
        long_lines = sum(len(line) > 100 for line in lines)

        if long_lines:
            readability -= 5
            suggestions.append("Reduce long lines for better readability.")

        # -----------------------------------
        # Missing Comments
        # -----------------------------------
        comments = sum(
            line.strip().startswith("#")
            for line in lines
        )

        if comments == 0:
            documentation -= 20
            suggestions.append("Add comments to improve documentation.")

        # -----------------------------------
        # Too Many Print Statements
        # -----------------------------------
        prints = len(re.findall(r"\bprint\s*\(", code))

        if prints > 5:
            maintainability -= 5
            suggestions.append("Reduce unnecessary print statements.")

        # -----------------------------------
        # eval()
        # -----------------------------------
        if "eval(" in code:
            security -= 30
            suggestions.append("Avoid using eval(); it is a security risk.")

        # -----------------------------------
        # exec()
        # -----------------------------------
        if "exec(" in code:
            security -= 30
            suggestions.append("Avoid using exec(); it is unsafe.")

        # -----------------------------------
        # Nested Loops
        # -----------------------------------
        loops = len(re.findall(r"\bfor\b|\bwhile\b", code))

        if loops > 5:
            performance -= 10
            suggestions.append("High number of loops may affect performance.")

        # -----------------------------------
        # Very Large File
        # -----------------------------------
        if len(lines) > 300:
            maintainability -= 10
            suggestions.append("Split large files into smaller modules.")

        # -----------------------------------
        # Function Names
        # -----------------------------------
        bad_names = re.findall(
            r"def\s+[a-zA-Z]?\(",
            code
        )

        if bad_names:
            readability -= 5
            suggestions.append("Use descriptive function names.")

        # -----------------------------------
        # Overall Score
        # -----------------------------------
        score = (
            readability +
            performance +
            security +
            maintainability +
            documentation
        ) // 5

        return {

            "overall": score,

            "readability": readability,

            "performance": performance,

            "security": security,

            "maintainability": maintainability,

            "documentation": documentation,

            "suggestions": suggestions

        }