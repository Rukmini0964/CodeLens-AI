# ==========================================================
# IMPORTS
# ==========================================================

import json
import requests
import streamlit as st
from streamlit_ace import st_ace

from backend.parser.language_detector import detect_language
from backend.report.pdf_generator import generate_pdf

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="CodeLens AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================
# Chat Session State
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# SESSION STATE
# ==========================================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "result" not in st.session_state:
    st.session_state.result = {}
    # Store code in session state
if "code" not in st.session_state:
    st.session_state.code = ""

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{
    background:#f5f5f5;
    border-radius:12px;
    padding:15px;
    border:1px solid #e0e0e0;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    font-weight:bold;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.title("💻 CodeLens AI")

st.markdown(
"""
### AI Powered Code Explainer & Reviewer

Analyze source code using AI.

✔ Explanation

✔ Bug Detection

✔ Optimization

✔ Complexity Analysis

✔ Code Quality Score

✔ PDF Report
"""
)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙ Settings")

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript"
        ]
    )

    uploaded_file = st.file_uploader(
        "📂 Upload Code",
        type=[
            "py",
            "java",
            "cpp",
            "js"
        ]
    )

    st.divider()

    st.success("🤖 Model")

    st.write("Llama 3.1 8B Instant")

    st.divider()

if st.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()

    st.info(
        """
Features

• Explain Code

• Review Code

• Detect Bugs

• Optimize Code

• Complexity Analysis

• Code Quality Score

• Download PDF Report
"""
    )

# ==========================================================
# LOAD FILE
# ==========================================================

if uploaded_file is not None:

    language = detect_language(uploaded_file.name)

    st.success(f"Detected Language: {language}")

    st.session_state.code = uploaded_file.read().decode("utf-8")
# ==========================================================
# CODE EDITOR
# ==========================================================

st.subheader("📝 Code Editor")

code = st_ace(
    value=st.session_state.code,
    language=language.lower(),
    theme="monokai",
    height=500,
    font_size=15,
    key="editor"
)

# Save edits back into session state
st.session_state.code = code

# ==========================================================
# CODE METRICS
# ==========================================================

line_count = len(code.splitlines()) if code else 0

word_count = len(code.split()) if code else 0

char_count = len(code) if code else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Language", language)

with col2:
    st.metric("Lines", line_count)

with col3:
    st.metric("Words", word_count)

with col4:
    st.metric("Characters", char_count)

st.divider()
# ==========================================================
# ANALYZE BUTTON
# ==========================================================

if st.button("🚀 Analyze Code", use_container_width=True):

    if not code.strip():

        st.warning("⚠ Please enter or upload some code.")

    else:

        payload = {
            "language": language,
            "code": code
        }

        progress = st.progress(0)

        try:

            with st.spinner("🤖 CodeLens AI is analyzing your code..."):

                progress.progress(10)

                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json=payload,
                    timeout=120
                )

                progress.progress(50)

            if response.status_code == 200:

               progress.progress(100)

               st.success("✅ Analysis Completed Successfully!")

               result = response.json()

               st.session_state.analysis = True
               st.session_state.result = result
            else:

                    st.error(
                        f"Backend Error ({response.status_code})"
                    )

                    st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                """
Cannot connect to FastAPI.

Run:

uvicorn main:app --reload
                """
            )

        except requests.exceptions.Timeout:

            st.error(
                "Request Timeout. Please try again."
            )

        except Exception as e:

            st.error(f"Unexpected Error:\n\n{e}")


# ==========================================================
# LOAD RESULT FROM SESSION STATE
# ==========================================================

if st.session_state.analysis:

    result = st.session_state.result

    language_result = result.get("language", language)

    explanation = result.get("explanation", "")

    review = result.get("review", "")

    bugs = result.get("bugs", "")

    optimization = result.get("optimization", "")

    complexity = result.get("complexity", "")

    quality = result.get("quality", {})

    overall_score = quality.get("overall", 0)

    readability = quality.get("readability", 0)

    performance = quality.get("performance", 0)

    security = quality.get("security", 0)

    maintainability = quality.get("maintainability", 0)

    documentation = quality.get("documentation", 0)

    quality_suggestions = quality.get("suggestions", [])
    # ==========================================================
# DISPLAY RESULTS
# ==========================================================

if st.session_state.analysis:

    st.divider()

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Explanation",
        "📝 Review",
        "🐞 Bugs",
        "⚡ Optimization",
        "📈 Complexity",
        "⭐ Quality"
    ])

    # =====================================================
    # EXPLANATION
    # =====================================================

    with tab1:

        st.subheader("📖 Code Explanation")

        if explanation:
            st.write(explanation)
        else:
            st.info("No explanation available.")

    # =====================================================
    # REVIEW
    # =====================================================

    with tab2:

        st.subheader("📝 Code Review")

        if review:
            st.write(review)
        else:
            st.info("No review available.")

    # =====================================================
    # BUG DETECTION
    # =====================================================

    with tab3:

        st.subheader("🐞 Bug Detection")

        if bugs:

            if isinstance(bugs, list):

                for bug in bugs:
                    st.error(f"• {bug}")

            else:
                st.write(bugs)

        else:
            st.success("✅ No bugs detected.")

    # =====================================================
    # OPTIMIZATION
    # =====================================================

    with tab4:

        st.subheader("⚡ Optimization Suggestions")

        if optimization:

            if isinstance(optimization, list):

                for item in optimization:
                    st.success(item)

            else:
                st.write(optimization)

        else:
            st.info("No optimization suggestions.")

    # =====================================================
    # COMPLEXITY
    # =====================================================

    with tab5:

        st.subheader("📈 Complexity Analysis")

        if isinstance(complexity, dict):

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Time Complexity",
                    complexity.get("time", "Unknown")
                )

            with col2:
                st.metric(
                    "Space Complexity",
                    complexity.get("space", "Unknown")
                )

            if complexity.get("description"):
                st.write(complexity["description"])

        else:
            st.write(complexity)

    # =====================================================
    # CODE QUALITY DASHBOARD
    # =====================================================

    with tab6:

        st.subheader("⭐ Code Quality Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Overall Score",
                f"{overall_score}/100"
            )

        with col2:

            if overall_score >= 90:
                grade = "A+"
            elif overall_score >= 80:
                grade = "A"
            elif overall_score >= 70:
                grade = "B"
            elif overall_score >= 60:
                grade = "C"
            else:
                grade = "D"

            st.metric("Grade", grade)

        with col3:

            if overall_score >= 80:
                status = "🟢 Excellent"
            elif overall_score >= 60:
                status = "🟡 Good"
            else:
                status = "🔴 Needs Improvement"

            st.metric("Status", status)

        st.progress(overall_score / 100)

        st.divider()

        st.subheader("📊 Quality Metrics")

        st.write("**Readability**")
        st.progress(readability / 100)
        st.write(f"{readability}%")

        st.write("**Performance**")
        st.progress(performance / 100)
        st.write(f"{performance}%")

        st.write("**Security**")
        st.progress(security / 100)
        st.write(f"{security}%")

        st.write("**Maintainability**")
        st.progress(maintainability / 100)
        st.write(f"{maintainability}%")

        st.write("**Documentation**")
        st.progress(documentation / 100)
        st.write(f"{documentation}%")

        st.divider()

        st.subheader("💡 AI Suggestions")

        if quality_suggestions:

            for suggestion in quality_suggestions:
                st.info(suggestion)

        else:

            st.success("🎉 Excellent! No quality issues detected.")
            st.divider()
# =====================================
# AI CHAT ASSISTANT
# =====================================

if st.session_state.analysis:

    st.divider()
    st.header("💬 AI Coding Assistant")

    st.info("""
You can ask questions like:

• Explain line 20
• Can this code be optimized?
• Convert this to Java
• What is the time complexity?
• Generate unit tests
• Explain this function
""")

    # Show previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Create the question variable
    question = st.chat_input("Ask anything about your uploaded code...")

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        payload = {
            "language": language,
            "code": code,
            "question": question
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json=payload,
                timeout=120
            )

            if response.status_code == 200:
                answer = response.json().get("answer", "No response received.")
            else:
                answer = f"Backend Error ({response.status_code})"

        except Exception as e:
            answer = f"Error: {e}"

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()
# =====================================
# PDF DOWNLOAD, JSON EXPORT & FOOTER
# =====================================

if st.session_state.analysis:

    st.divider()

    st.subheader("📄 Export Analysis")

    # Generate PDF
    # -------------------------------
    try:

        pdf_path = generate_pdf(
            language=language_result,
            code=code,
            explanation=explanation,
            review=review,
            bugs=bugs,
            optimization=optimization,
            complexity=complexity
        )

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="CodeLens_AI_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as e:

        st.warning(f"Unable to generate PDF.\n\n{e}")

    # -------------------------------
    # JSON Export
    # -------------------------------

    report = {
        "language": language_result,
        "code": code,
        "explanation": explanation,
        "review": review,
        "bugs": bugs,
        "optimization": optimization,
        "complexity": complexity,
        "quality": quality
    }

    st.download_button(
        label="📥 Download JSON Report",
        data=json.dumps(report, indent=4),
        file_name="CodeLens_AI_Report.json",
        mime="application/json",
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # SUMMARY
    # =====================================================

    st.subheader("📋 Analysis Summary")

    summary = f"""
Language            : {language_result}

Overall Score       : {overall_score}/100

Readability         : {readability}%

Performance         : {performance}%

Security            : {security}%

Maintainability     : {maintainability}%

Documentation       : {documentation}%
"""

    st.code(summary)

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
---
<div style="text-align:center">

## 💻 CodeLens AI

### AI-Powered Code Explainer & Reviewer

Built with ❤️ using

**Python • Streamlit • FastAPI • LangChain • Groq • Llama 3.1**

---

© 2026 CodeLens AI | Final Year Project

</div>
""",
    unsafe_allow_html=True
)