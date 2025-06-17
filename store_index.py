from src.helper import load_pdf_file, text_split,download_hugging_face
from dotenv import load_dotenv
import os
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore


load_dotenv()

PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY']= PINECONE_API_KEY


extrac= load_pdf_file(data= 'Data/')
chunks= text_split(extrac)
emb= download_hugging_face()


pc = Pinecone(api_key='pcsk_6vhUGc_PP8vzP1KBW1kxBokMuVDHYpxD7AEKEzUCFY3YWdoCsQrBeGAjFqwRbj1b5RdsE2')

index_name = "testbot"

pc.create_index(
        name=index_name,
        dimension= 384,
        metric='cosine',
        spec=ServerlessSpec(
            cloud="aws",
        region="us-east-1"

        )
       
    )


docsearch= PineconeVectorStore.from_documents(
    documents=chunks,
    index_name= index_name,
    embedding= emb
)




