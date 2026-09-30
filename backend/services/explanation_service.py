from backend.reviewer.explain import CodeExplainer
from backend.reviewer.review import CodeReviewer
from backend.reviewer.bug_detector import BugDetector
from backend.reviewer.optimizer import CodeOptimizer
from backend.reviewer.complexity import ComplexityAnalyzer


class ExplanationService:

    @staticmethod
    def analyze(language: str, code: str):

        explanation = CodeExplainer.explain(
            language,
            code
        )

        review = CodeReviewer.review(
            language,
            code
        )

        bugs = BugDetector.detect(
            language,
            code
        )

        optimization = CodeOptimizer.optimize(
            language,
            code
        )

        complexity = ComplexityAnalyzer.analyze(
            language,
            code
        )

        return {
            "language": language,
            "explanation": explanation,
            "review": review,
            "bugs": bugs,
            "optimization": optimization,
            "complexity": complexity
        }