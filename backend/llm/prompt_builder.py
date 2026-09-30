from config.prompts import (
    CODE_EXPLANATION_PROMPT,
    CODE_REVIEW_PROMPT,
    COMPLEXITY_PROMPT,
    OPTIMIZER_PROMPT,
    BUG_PROMPT,
    BEGINNER_PROMPT
)


def explanation_prompt(language, code):
    return CODE_EXPLANATION_PROMPT.format(
        language=language,
        code=code
    )


def review_prompt(language, code):
    return CODE_REVIEW_PROMPT.format(
        language=language,
        code=code
    )


def complexity_prompt(language, code):
    return COMPLEXITY_PROMPT.format(
        language=language,
        code=code
    )


def optimizer_prompt(language, code):
    return OPTIMIZER_PROMPT.format(
        language=language,
        code=code
    )


def bug_prompt(language, code):
    return BUG_PROMPT.format(
        language=language,
        code=code
    )


def beginner_prompt(language, code):
    return BEGINNER_PROMPT.format(
        language=language,
        code=code
    )