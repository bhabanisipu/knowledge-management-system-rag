from app.rag.loader import DocumentLoader
from app.rag.splitter import DocumentSplitter

loader = DocumentLoader()
documents = loader.load_document("uploads/employee_handbook.txt")

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)