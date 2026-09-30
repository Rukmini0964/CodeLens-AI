from backend.llm.chains import analyze_complexity


class ComplexityAnalyzer:

    @staticmethod
    def analyze(language: str, code: str):

        return analyze_complexity(
            language=language,
            code=code
        )