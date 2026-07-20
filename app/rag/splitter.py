try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
except Exception:
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except Exception as e:
        raise ImportError(
            "RecursiveCharacterTextSplitter not available. Install 'langchain' or 'langchain-text-splitters'."
        ) from e


class DocumentSplitter:

    def __init__(self, chunk_size=500, chunk_overlap=100):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)