from backend.reviewer.review import CodeReviewer


class ReviewService:

    @staticmethod
    def review(language: str, code: str):

        return CodeReviewer.review(
            language,
            code
        )