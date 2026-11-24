import sys
from pathlib import Path

import streamlit as st
import pymupdf

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.extraction.policy_extractor import extract_policy_details

st.set_page_config(
    page_title="PolicyGraph-AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PolicyGraph-AI")
st.subheader("Intelligent Policy Document Analyzer")

st.write("Upload a scholarship policy PDF to extract important information.")

uploaded_file = st.file_uploader(
    "Upload your policy PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    try:
        with pymupdf.open(
            stream=uploaded_file.getvalue(),
            filetype="pdf"
        ) as pdf:
            extracted_text = "\n".join(
                page.get_text() for page in pdf
            )

        details = extract_policy_details(extracted_text)

        st.success("Policy document processed successfully!")

        st.header("Extracted Policy Details")

        for key, value in details.items():
            st.write(
                f"*{key.replace('_', ' ').title()}:* "
                f"{value if value is not None else 'Not found'}"
            )

        with st.expander("View extracted PDF text"):
            st.text(extracted_text)

    except Exception as error:
        st.error(f"Could not process PDF: {error}")