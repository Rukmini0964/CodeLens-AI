from backend.chat.chat_service import ChatService
from fastapi import FastAPI
from pydantic import BaseModel

from backend.reviewer.explain import CodeExplainer
from backend.reviewer.review import CodeReviewer
from backend.reviewer.bug_detector import BugDetector
from backend.reviewer.optimizer import CodeOptimizer
from backend.reviewer.complexity import ComplexityAnalyzer

from backend.services.quality_service import QualityService


app = FastAPI(
    title="CodeLens AI",
    version="1.0"
)


# -------------------------------
# Request Model
# -------------------------------
class CodeRequest(BaseModel):
    language: str
    code: str
class ChatRequest(BaseModel):
    language: str
    code: str
    question: str


# -------------------------------
# Initialize Services
# -------------------------------
explainer = CodeExplainer()
reviewer = CodeReviewer()
bug_detector = BugDetector()
optimizer = CodeOptimizer()
complexity = ComplexityAnalyzer()
quality = QualityService()
chat = ChatService()


# -------------------------------
# Home Route
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to CodeLens AI 🚀"
    }


# -------------------------------
# Analyze Route
# -------------------------------
@app.post("/analyze")
def analyze(request: CodeRequest):

    explanation = explainer.explain(
        request.code,
        request.language
    )

    review = reviewer.review(
        request.code,
        request.language
    )

    bugs = bug_detector.detect(
        request.code,
        request.language
    )

    optimization = optimizer.optimize(
        request.code,
        request.language
    )

    complexity_result = complexity.analyze(
    request.language,
    request.code
)

    quality_result = quality.analyze(
    request.code
)
    
    

    return {

        "language": request.language,

        "explanation": explanation,

        "review": review,

        "bugs": bugs,

        "optimization": optimization,

        "complexity": complexity_result,

        "quality": quality_result

    }
@app.post("/chat")
def chat_endpoint(request: ChatRequest):

    answer = chat.ask(
        language=request.language,
        code=request.code,
        question=request.question
    )

    return {
        "answer": answer
    }