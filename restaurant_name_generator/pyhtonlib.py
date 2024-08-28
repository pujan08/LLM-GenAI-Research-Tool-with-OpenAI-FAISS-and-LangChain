import nltk
from langchain_community.document_loaders import UnstructuredURLLoader

# Download 'punkt' tokenizer data for nltk
nltk.download('punkt')

# List of URLs to fetch
urls = ["https://en.wikipedia.org/wiki/Neural_network_(machine_learning)"]

try:
    # Create an UnstructuredURLLoader instance
    loader = UnstructuredURLLoader(urls=urls)

    # Load data from URLs
    data = loader.load()

    # Print the number of documents loaded
    print(f"Number of documents loaded: {len(data)}")
except Exception as e:
    print(f"Error: {e}")
