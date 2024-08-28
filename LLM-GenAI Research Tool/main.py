import os
import streamlit as st
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import unstructured
import langchain_community  # Ensure this module is installed and accessible

from openapi_key import api_key  # Import your API key from a local file

os.environ['OPENAI_API_KEY'] = api_key  # Set the API key as an environment variable

st.title("News Research Tool")

st.sidebar.title("News Article URLs")

# Initialize an empty list to store URLs entered by the user
urls = []
for i in range(3):
    # Capture URLs from sidebar input fields
    url = st.sidebar.text_input(f"URL {i + 1}")
    if url:  # Add the URL to the list only if it's not empty
        urls.append(url)

# Button to trigger the URL processing
process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_index_openai"  # Path to save the FAISS vector store
main_placeholder = st.empty()  # Placeholder to update status messages on the main page

# Process the URLs when the button is clicked
if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)  # Load data from the provided URLs
    main_placeholder.text("Data loading... Started...")  # Update status

    data = loader.load()  # Load the data from the URLs
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],  # Custom separators for text splitting
        chunk_size=1000  # Define chunk size for splitting the text
    )

    main_placeholder.text("Data loading... In Progress...")  # Update status
    docs = text_splitter.split_documents(data)  # Split the loaded data into chunks

    embeddings = OpenAIEmbeddings()  # Initialize OpenAI embeddings
    vectorstore_openai = FAISS.from_documents(docs, embeddings)  # Create a FAISS vector store

    main_placeholder.text("Data processing... Finalizing...")  # Update status
    time.sleep(2)  # Add a delay to simulate processing time

    # Save the FAISS index to a directory for later use
    vectorstore_openai.save_local(file_path)

    main_placeholder.text("Data processing... Completed!")  # Final status message

# Capture a user query for retrieval
query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        # Load the FAISS vector store if it exists, with dangerous deserialization allowed
        vectorstore_openai = FAISS.load_local(file_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

        # Initialize the LLM (assuming `llm` is previously defined)
        llm = OpenAI()  # Make sure to define your LLM here

        # Create a retrieval chain with the FAISS vector store
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore_openai.as_retriever())

        # Perform the query and retrieve the result
        result = chain({"question": query}, return_only_outputs=True)

        # Display the answer
        st.header("Answer")
        st.write(result["answer"])

        # Display the sources
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)
