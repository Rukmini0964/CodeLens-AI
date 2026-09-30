from pathlib import Path


EXTENSION_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cs": "C#",
    ".go": "Go",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin"
}


def detect_language(filename: str) -> str:
    """
    Detect programming language from filename.
    """

    extension = Path(filename).suffix.lower()

    return EXTENSION_MAP.get(extension, "Unknown")