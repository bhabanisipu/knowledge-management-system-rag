from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
)


class DocumentLoader:

    def load_document(self, file_path: str):

        if file_path.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")

        elif file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)

        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)

        else:
            raise ValueError("Unsupported file format.")

        documents = loader.load()

        return documents