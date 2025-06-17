from flask import Flask, render_template, jsonify, request
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src.prompt import *
from src.helper import download_hugging_face



app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY']= PINECONE_API_KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


emb= download_hugging_face()
 

index_name = "testbot"

from langchain_pinecone import PineconeVectorStore
docsearch= PineconeVectorStore.from_existing_index(
    index_name= index_name,
    embedding= emb
)


re= docsearch.as_retriever(search_type='similarity', search_kwargs= {'k':3})

from langchain_groq import ChatGroq
llm = ChatGroq(api_key=GROQ_API_KEY, model_name= 'llama3-70b-8192')



prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template,
)

# Create chain
question_answer_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)
rag_chain = RetrievalQA(combine_documents_chain=question_answer_chain, retriever=re)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message') if data else None

    try:
        result = rag_chain.invoke({"query": user_message})
        bot_reply = result['result']
    except Exception as e:
        bot_reply = "Sorry, I couldn't process that right now."

    return jsonify({
        "reply": bot_reply
    })

    
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8080, debug= True)


