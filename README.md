# Statista Case Study

Submission for the 
[Statista Case Study](docs/Case_Study_-_Software.pdf).

## Analysis

Statista is a large provider of data looking to create an API to expose to RAG-like (Retrieval-Augmented Generation) applications. Since the data is Statista's key intellectual property, it is assumed the role of the Statista API is to provide the data to augment LLMs, not to provide the LLM feature itself. Below is a workflow diagram of a simple RAG application. The provider application is any application that wishes to use Statista data to augment its LLM.

![Workflow](docs/workflow.png "Workflow")

The Statista API will sit at the data retrieval layer of the RAG. It will return relevant documents that can be used to power an LLM allowing it to produce better, more relevant results.

### Document Stores

A crucial part of the Statista API’s usefulness will be its ability to return relevant results from a large database of over 1 million statistics and 80,000 topics. Depending on the nature of the data different database types can be used. Although the sample data for this case study has a well defined schema that could be used in a relational databse, this demo will implement the search on a vector database. A vector database was chosen because Statista has a large amount of data across many topics that may be unstructured. It is also possible for an endpoint to query multiple database if the need arises.


## Code

A small demo has been created to illustrate how an API can query a vector store to retrieve documents for RAG applications. Key features of the demo code are:

* Written in Python 3.12
* Faker to create mock data
* FastAPI for the REST API
* ChromaDB for the Vector Store

### Instructions

1. Install

    ```bash
    pip install -r requirements.txt
    ```

1. Populate the mock data

    ```bash
    python vector_store.py
    ```

1. Run

    ```bash
    fastapi dev main.py
    ```

1. Visit the api docs page and use the swagger UI to test endpoint

    http://127.0.0.1:8000/docs

