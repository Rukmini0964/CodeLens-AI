from backend.llm.chains import detect_bugs


class BugDetector:

    @staticmethod
    def detect(language: str, code: str):

        return detect_bugs(
            language=language,
            code=code
        )