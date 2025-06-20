# Medical ChatBot

An AI-powered medical assistant that provides accurate medical information by analyzing a medical knowledge base. Built with Flask and powered by the Groq LLM and Pinecone vector database.

## Features
- **Medical Knowledge Base**: Automatically processes and indexes medical information from PDF documents  
- **Intelligent Querying**: Uses RAG (Retrieval Augmented Generation) for accurate responses  
- **Vector Search**: Efficient information retrieval using Pinecone  
- **AI-Powered Responses**: Generates accurate medical information using Groq's LLaMA3 model  
- **Web Interface**: User-friendly chat interface built with Flask  

## Tech Stack
- **Frontend**: Flask + HTML/CSS  
- **Language Model**: Groq (llama3-70b-8192)  
- **Vector Database**: Pinecone  
- **Embeddings**: HuggingFace (sentence-transformers)  
- **PDF Processing**: LangChain's PyPDFLoader  
- **Environment Management**: Python dotenv  

## Setup
1. **Clone the repository**  
2. **Install dependencies**  
3. **Set up environment variables**: Create a `.env` file in the root directory with the following configurations  
4. **Store your medical knowledge base**: Place your medical PDF documents in the `Data` directory  
5. **Index your documents**  
6. **Run the application**  

The application will be available at [http://localhost:8080](http://localhost:8080)

## Project Structure
```
Medical-ChatBot/
├── Data/
│   └── Medical_book.pdf
├── src/
│   ├── __init__.py
│   ├── helper.py        # Utility functions for document processing
│   └── prompt.py        # LLM prompt templates
├── templates/
│   └── index.html       # Chat interface template
├── static/
├── app.py              # Main Flask application
├── store_index.py      # Document indexing script
├── setup.py            # Project setup configuration
└── README.md
```

## Usage
1. Open your web browser and navigate to [http://localhost:8080](http://localhost:8080)  
2. Type your medical query in the chat interface  
3. Receive AI-generated responses based on the medical knowledge base  

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions and support, please contact: **karthikmsarma@gmail.com**
