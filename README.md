# LLM-GenAI-Research-Tool-with-OpenAI-FAISS-and-LangChain
Harnessing LLMs and GenAI for Efficient Research with OpenAI, FAISS, and LangChain Integration

This project is a comprehensive research tool designed to streamline the analysis of news articles using cutting-edge AI technologies. By integrating Large Language Models (LLMs) with General AI (GenAI) through OpenAI's APIs, the tool allows users to process and retrieve relevant information from multiple news sources. Utilizing FAISS for efficient vector storage and LangChain for seamless data handling, this tool exemplifies the power of modern AI in transforming unstructured data into actionable insights. Ideal for researchers and data enthusiasts, the project demonstrates advanced techniques in natural language processing and information retrieval.
\n
**Steps to Create and Run the LLM-GenAI Research Tool**
**1. Set Up the Development Environment**
Clone the Repository:
	git clone https://github.com/yourusername/LLM-GenAI-Research-Tool.git
	cd LLM-GenAI-Research-Tool
**2. Install Required Packages**
Install the necessary Python packages:
	pip install streamlit langchain openai faiss-cpu unstructured nltk
**3. Set Up OpenAI API Key**
Create a file named openapi_key.py in the project root directory:
	# openapi_key.py
	api_key = "your_openai_api_key_here"
**4. Run the Streamlit Application**
	streamlit run main.py
**5. Usage**
	Input URLs: Enter up to three URLs of news articles in the sidebar.
	Process Data: Click the "Process URLs" button to load, split, and embed the article content.
	Ask Questions: Use the input field to ask questions about the content. The app will provide answers and list sources.
**Additional Notes**
Security Warning: The project uses FAISS vector storage, which involves serializing and deserializing data. Ensure you trust the source when reloading serialized files.
Testing: Test the application in a local environment before deploying or sharing it.
