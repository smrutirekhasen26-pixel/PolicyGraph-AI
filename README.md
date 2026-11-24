PolicyGraph-AI

A Python-based policy document analyzer that extracts important information from government and scholarship policy PDF documents.

Features

- Upload policy PDF documents.
- Extract text from PDF files.
- Identify important policy details:
  - Eligibility requirements
  - Minimum age
  - Scholarship amount
  - Application deadline
- Display extracted information in an interactive Streamlit dashboard.
- Handle invalid PDF uploads with error messages.

Technologies Used

- Python
- Streamlit
- PyMuPDF
- Regular Expressions
- VS Code

Project Structure

PolicyGraph-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── raw/
│       ├── sample_policy.pdf
│       └── sample_policy_test_2.pdf
│
└── src/
    └── extraction/
        └── policy_extractor.py

How to Run

1. Clone or download this project.
2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

python -m streamlit run app.py

4. Open the local URL displayed in the terminal.
5. Upload a policy PDF to view the extracted information.

Testing

The application has been tested with:

- Valid policy PDF documents.
- Different policy details.
- Invalid PDF files.

Future Enhancements

- AI-powered policy information extraction.
- Policy version comparison.
- Conflict detection.
- Knowledge graph visualization.
- Citizen impact analysis.

Project Status

Initial working MVP completed. Advanced features are planned for future development.