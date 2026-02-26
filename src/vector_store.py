from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

class VectorStore:
    """Wrapper around Chroma to provide a retriever."""
    def __init__(self, persist_directory: str):
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory=self.persist_directory,
                         embedding_function=self.embeddings)

    def get_retriever(self):
        return self.db.as_retriever()


class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vector_store(self):
        loader = CSVLoader(file_path=self.csv_path, encoding='utf-8', metadata_columns=[])
        data = loader.load()
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)
        db = Chroma.from_documents(texts, self.embeddings, persist_directory=self.persist_dir)
        db.persist()

    def build_vector_store(self):
        return self.build_and_save_vector_store()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)
        