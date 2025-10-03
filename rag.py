from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os



if "GROQ_API_KEY" in os.environ:
    api_key = os.environ["GROQ_API_KEY"]
else:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

CHUNK_SIZE = 1000
EMBEDDING_MODEL = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate_docs"

llm = None
vector_store = None

def initialize_components():
    global llm, vector_store
    if llm is None:
            
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    if vector_store is None:    
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )
        vector_store = Chroma(
            persist_directory=str(VECTORSTORE_DIR),
            collection_name=COLLECTION_NAME,
            embedding_function=ef
        )

def process_urls(urls):
    """
    This function scrapes data from a url and store it in a vector database.
    :param urls: input urls
    :return: None
    """
    yield "Starting processing of URLs..."
    initialize_components()

    vector_store.reset_collection()

    yield "Loading data from URLs..."
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    yield f"Loaded {len(data)} documents from the URLs"
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", ""], chunk_size=CHUNK_SIZE)
    docs = text_splitter.split_documents(data)

    
    yield "Adding to vector store..."
    vector_store.add_documents(docs, ids=[ str(uuid4()) for _ in range(len(docs)) ])


def generate_answer(query):
    """
    This function generates an answer to a query using the vector database and LLM.
    :param query: input query
    :return: answer
    """

    if not vector_store:
        raise RuntimeError("Vector store is not initialized. Please run process_urls() first.")
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever()
    )
    result = chain.invoke({"question": query}, return_only_outputs=True)
    sources = result.get("sources", "")

    return result["answer"], sources 


if __name__ == "__main__":
    urls = [
        "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html",
        ]

    for msg in process_urls(urls):
        print(msg)

    answer, sources = generate_answer("Tell me what was the 30 year fixed mortgage rate along with the date?")
    print(f"Answer: {answer}\nSources: {sources}")