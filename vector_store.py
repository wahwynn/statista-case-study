import json

from langchain_chroma import Chroma
from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings

from mock_data import MOCK_DATA_FILE, generate_mock_data

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

COLLECTION_NAME = "mock_data_chroma"
PERSIST_DIR = f"./{COLLECTION_NAME}.db"


def get_vector_store_db():
    return Chroma(
        embedding_function=embedding_function,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIR,
    )


def find_in_vector_store(query, k=5):
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return retriever.get_relevant_documents(query)


def docs_to_json(docs):
    return [json.loads(doc.page_content) for doc in docs]


# Initial load of the vectordb
vectordb = get_vector_store_db()

if __name__ == "__main__":
    all_documents = vectordb.get()["documents"]
    total_records = len(all_documents)
    print(f"Total records in the collection: {total_records}")

    if total_records == 0:
        generate_mock_data()
        loader = JSONLoader(
            file_path=MOCK_DATA_FILE, jq_schema=".[]", text_content=False
        )
        documents = loader.load()

        db = Chroma.from_documents(
            documents,
            embedding_function,
            collection_name=COLLECTION_NAME,
            persist_directory=PERSIST_DIR,
        )

        all_documents = db.get()["documents"]
        total_records = len(all_documents)
        print(f"Total records in the db: {total_records}")
    else:
        print(f"Data already populated with {total_records} documents. Sample:")
        print(all_documents[:5])
