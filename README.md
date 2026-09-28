# ai-hire

📁 Project Structure
my-resume-screener/
│
├── .gitattributes       # Git configuration for uniform line endings
├── app.py               # Streamlit application layout and frontend UI
├── requirements.txt     # Python project dependencies 
└── utils.py             # In-memory document extraction and algorithmic utilities

🛠️ Tech Stack
* Frontend & UI Engine: Streamlit 
* Natural Language Processing (NLP): Scikit-Learn (TF-IDF) 
* Mathematical Vector Matching: Scikit-Learn (Cosine Similarity)
* PDF Extraction Parser: pdfminer.six
* Word Processing Parser: python-docx
* Data Synthesis & Matrices: pandas


✅ To Run Locally
 1. Open Terminal or Command Prompt
Navigate into your root directory containing the application files:
bash
cd path/to/my-resume-screener
 2. Create a Virtual Environment
Isolate your package dependencies so they do not conflict with other system libraries.
 Mac/Linux:
python3 -m venv venv
 Windows:
cmd
python -m venv venv
 3. Activate the Environment
Turn on your newly made virtual space before you begin package installation.
 Mac/Linux:
bash
source venv/bin/activate
 Windows(Command Prompt):
cmd
venv\Scripts\activate
 Windows (PowerShell):
powershell
.\venv\Scripts\Activate.ps1
 4. Install Dependencies
Run a recursive installation on the structured package requirements tracker file:
bash
pip install -r requirements.txt
 5. Launch the Web Application
Fire up your localized rendering stream engine server instance:
bash
streamlit run app.py
                              ------------------------------------------------
Your system will automatically launch a web browser window pointing to your local environment at http://localhost:8501.


