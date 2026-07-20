from app.rag.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_document("uploads/employee_handbook.txt")

print(documents)

print()
print()

print(documents[0].page_content)