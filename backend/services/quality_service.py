from backend.reviewer.quality_score import CodeQualityScorer


class QualityService:

    def __init__(self):
        self.scorer = CodeQualityScorer()

    def analyze(self, code: str):
        """
        Analyze the quality of the given source code.
        Returns a dictionary containing:
        - overall score
        - readability
        - performance
        - security
        - maintainability
        - documentation
        - suggestions
        """
        return self.scorer.calculate(code)