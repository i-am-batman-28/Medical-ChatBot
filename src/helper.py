from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_pdf_file(data):
    loader= DirectoryLoader(
        data, glob= '*.pdf', loader_cls= PyPDFLoader)
    doc= loader.load()
    return doc
    


def text_split(exac):
    spl= RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 20)
    chunks= spl.split_documents(exac)
    return chunks


def download_hugging_face():
    emb= HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2'
)
    return emb


