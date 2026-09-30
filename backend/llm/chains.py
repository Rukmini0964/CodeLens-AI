from backend.llm.groq_client import llm
from backend.llm.prompt_builder import (
    explanation_prompt,
    review_prompt,
    complexity_prompt,
    optimizer_prompt,
    bug_prompt,
    beginner_prompt
)
from backend.llm.output_parser import parse_output


def explain_code(language, code):

    prompt = explanation_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)


def review_code(language, code):

    prompt = review_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)


def analyze_complexity(language, code):

    prompt = complexity_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)


def optimize_code(language, code):

    prompt = optimizer_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)


def detect_bugs(language, code):

    prompt = bug_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)


def explain_for_beginner(language, code):

    prompt = beginner_prompt(language, code)

    response = llm.invoke(prompt)

    return parse_output(response)