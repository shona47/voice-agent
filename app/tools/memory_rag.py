
import chromadb
from sentence_transformers import SentenceTransformer

from app.llm.qwen import ask_llm


# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Create persistent ChromaDB
client = chromadb.PersistentClient(
    path="app/memory/chroma_db"
)

collection = client.get_or_create_collection(
    name="user_memory"
)


def store_memory(fact):

    # Convert fact into embedding
    embedding = embedding_model.encode(fact).tolist()

    # Create unique ID
    memory_id = f"memory_{collection.count() + 1}"

    collection.add(
        ids=[memory_id],
        documents=[fact],
        embeddings=[embedding]
    )

    return {
        "success": True,
        "message": "Memory stored successfully",
        "memory": fact,
        "memory_id": memory_id
    }


def list_memories():

    # Get all stored memories
    results = collection.get(
        include=["documents"]
    )

    ids = results.get("ids", [])
    documents = results.get("documents", [])

    if not ids:

        return {
            "success": True,
            "message": "No memories stored.",
            "memories": []
        }

    memories = []

    for memory_id, document in zip(ids, documents):

        memories.append({
            "id": memory_id,
            "memory": document
        })

    return {
        "success": True,
        "message": f"Found {len(memories)} memories.",
        "memories": memories
    }


def delete_memory(memory_id):

    # Check whether the memory exists
    results = collection.get(
        ids=[memory_id],
        include=["documents"]
    )

    ids = results.get("ids", [])

    if not ids:

        return {
            "success": False,
            "message": f"Memory '{memory_id}' not found."
        }

    # Delete the selected memory
    collection.delete(
        ids=[memory_id]
    )

    return {
        "success": True,
        "message": f"Memory '{memory_id}' deleted successfully."
    }


def retrieve_memory(query):

    # Check if there are any memories
    if collection.count() == 0:

        return {
            "success": True,
            "message": "No relevant memory found."
        }

    # Convert user's question into embedding
    query_embedding = embedding_model.encode(query).tolist()

    # Search for similar memories
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(3, collection.count())
    )

    documents = results.get("documents", [[]])[0]

    if not documents:

        return {
            "success": True,
            "message": "No relevant memory found."
        }

    # Combine retrieved memories
    context = "\n".join(
        f"- {document}"
        for document in documents
    )

    prompt = f"""
You are a helpful AI personal assistant.

Use the following retrieved memories to answer the user's question.

Retrieved memories:
{context}

User question:
{query}

Answer using only the relevant information from the retrieved memories.
If the memories do not contain the answer, say that you don't have that information.
"""

    answer = ask_llm(prompt)

    return {
        "success": True,
        "message": answer,
        "retrieved_memories": documents
    }


def memory_tool(parameters):

    action = parameters.get("action")
    content = parameters.get("content")

    if action == "store":

        return store_memory(content)

    elif action == "retrieve":

        return retrieve_memory(content)

    elif action == "list":

        return list_memories()

    elif action == "delete":

        return delete_memory(content)

    else:

        return {
            "success": False,
            "message": "Unknown memory action."
        }

