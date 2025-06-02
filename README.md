🤖 GenAI Patient Query Assistant
A conversational AI assistant for answering patient queries using healthcare data and GenAI technologies.

## 🚀 Features
Natural language queries on patient and claims data

Integrates with OpenAI GPT models via LangChain

Custom document indexing for fast retrieval

Easy-to-use web interface built with Streamlit

## ⚙️ Setup Instructions
Clone the repository
git clone https://github.com/VaishnaviUppula/genai_patient_query_assistant.git
cd genai_patient_query_assistant

Create and activate a Python virtual environment (recommended)
python -m venv venv

Windows
.\venv\Scripts\activate

macOS/Linux
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Create a .env file in the project root
This file will hold your environment variables such as API keys.

Example .env:
OPENAI_API_KEY=your_openai_api_key_here

⚠️ Keep your .env file secret and do NOT commit it to version control.

## Run the app
streamlit run app.py

## 🗂️ Project Structure
genai_patient_query_assistant/
├── app/
│   ├── app.py               # Main Streamlit app entrypoint
│   ├── langchain_helper.py  # LangChain utility functions
│   └── main.py              # Core logic for query processing
├── index_builder/
│   └── build_index.py       # FAISS-based document indexing
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys, etc.)
└── README.md                # Project documentation

## 💡 Usage
Open your browser at http://localhost:8501 after running the app.

Type your patient-related queries and get AI-powered responses instantly!

## 📄 License
This project is licensed under the MIT License.

## ✉️ Contact
Created by Vaishnavi Uppula