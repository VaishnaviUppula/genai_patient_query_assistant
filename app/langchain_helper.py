from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def load_and_split_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)

def create_faiss_vectorstore(docs, index_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)

def load_faiss_vectorstore(index_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(index_path, embeddings)

def get_answer_from_query(vectorstore, query):
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    result = qa_chain.run(query)
    return result

def load_faiss_vectorstore(index_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    # Set allow_dangerous_deserialization=True because you created the index locally and trust it
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
