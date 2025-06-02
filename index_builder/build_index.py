from langchain_helper import load_and_split_docs, create_faiss_vectorstore

# Replace this filename with your actual PDF file name
PDF_PATH = "health_insurance_pdf.pdf"

docs = load_and_split_docs(PDF_PATH)
create_faiss_vectorstore(docs)

print("✅ FAISS index created and saved locally.")
