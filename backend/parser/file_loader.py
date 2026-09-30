from pathlib import Path


SUPPORTED_FILES = [
    ".py",
    ".java",
    ".cpp",
    ".c",
    ".js",
    ".ts",
    ".cs",
    ".go",
    ".php",
    ".rb",
    ".swift",
    ".kt"
]


def load_code(file_path: str):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    if path.suffix.lower() not in SUPPORTED_FILES:
        raise ValueError("Unsupported file type.")

    return path.read_text(encoding="utf-8")