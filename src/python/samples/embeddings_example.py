"""
Azure OpenAI Embeddings Example

This module demonstrates how to generate text embeddings using Azure OpenAI
for semantic search, similarity comparison, and RAG applications.
"""

import os
import logging
from typing import Optional
import numpy as np

from openai import AzureOpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_azure_openai_client() -> AzureOpenAI:
    """
    Create and return an Azure OpenAI client with configuration from environment variables.
    
    Returns:
        AzureOpenAI: Configured Azure OpenAI client
    """
    load_dotenv()
    
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    if not endpoint or not api_key:
        raise ValueError(
            "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY environment variables must be set"
        )
    
    return AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version
    )


def get_embedding(
    client: AzureOpenAI,
    text: str,
    deployment_name: Optional[str] = None
) -> list[float]:
    """
    Generate an embedding vector for the given text.
    
    Args:
        client: Azure OpenAI client instance
        text: The text to embed
        deployment_name: Azure OpenAI embeddings deployment name
        
    Returns:
        list[float]: The embedding vector
    """
    deployment = deployment_name or os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")
    
    logger.info(f"Generating embedding for text ({len(text)} chars)")
    
    response = client.embeddings.create(
        model=deployment,
        input=text
    )
    
    embedding = response.data[0].embedding
    logger.info(f"Generated embedding with {len(embedding)} dimensions")
    
    return embedding


def get_embeddings_batch(
    client: AzureOpenAI,
    texts: list[str],
    deployment_name: Optional[str] = None
) -> list[list[float]]:
    """
    Generate embeddings for multiple texts in a single API call.
    
    Args:
        client: Azure OpenAI client instance
        texts: List of texts to embed
        deployment_name: Azure OpenAI embeddings deployment name
        
    Returns:
        list[list[float]]: List of embedding vectors
    """
    deployment = deployment_name or os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")
    
    logger.info(f"Generating embeddings for {len(texts)} texts")
    
    response = client.embeddings.create(
        model=deployment,
        input=texts
    )
    
    # Sort by index to ensure order matches input
    embeddings = [item.embedding for item in sorted(response.data, key=lambda x: x.index)]
    
    logger.info(f"Generated {len(embeddings)} embeddings")
    
    return embeddings


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1: First vector
        vec2: Second vector
        
    Returns:
        float: Cosine similarity score (-1 to 1)
    """
    a = np.array(vec1)
    b = np.array(vec2)
    
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_most_similar(
    query_embedding: list[float],
    document_embeddings: list[list[float]],
    documents: list[str],
    top_k: int = 3
) -> list[tuple[str, float]]:
    """
    Find the most similar documents to a query based on embeddings.
    
    Args:
        query_embedding: The query embedding vector
        document_embeddings: List of document embedding vectors
        documents: List of original documents
        top_k: Number of results to return
        
    Returns:
        list[tuple[str, float]]: List of (document, similarity_score) tuples
    """
    similarities = [
        (doc, cosine_similarity(query_embedding, doc_emb))
        for doc, doc_emb in zip(documents, document_embeddings)
    ]
    
    # Sort by similarity score descending
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:top_k]


def main():
    """Main function demonstrating Azure OpenAI embeddings usage."""
    try:
        # Initialize client
        client = get_azure_openai_client()
        logger.info("Azure OpenAI client initialized successfully")
        
        # Sample documents for semantic search
        documents = [
            "Prompt engineering involves designing effective prompts for AI models.",
            "Azure OpenAI provides enterprise-grade AI services in the cloud.",
            "Python is a popular programming language for machine learning.",
            "RAG combines retrieval systems with generative AI for accurate responses.",
            "Chain-of-thought prompting helps models reason through complex problems.",
            "The weather forecast predicts sunny skies for the weekend.",
        ]
        
        # Example 1: Generate embeddings for documents
        print("\n" + "=" * 50)
        print("Example 1: Generate Document Embeddings")
        print("=" * 50)
        
        document_embeddings = get_embeddings_batch(client, documents)
        print(f"Generated embeddings for {len(documents)} documents")
        print(f"Embedding dimension: {len(document_embeddings[0])}")
        
        # Example 2: Semantic search
        print("\n" + "=" * 50)
        print("Example 2: Semantic Search")
        print("=" * 50)
        
        query = "How do I write better prompts for AI?"
        query_embedding = get_embedding(client, query)
        
        results = find_most_similar(
            query_embedding,
            document_embeddings,
            documents,
            top_k=3
        )
        
        print(f"Query: {query}")
        print("\nTop matches:")
        for i, (doc, score) in enumerate(results, 1):
            print(f"  {i}. (Score: {score:.4f}) {doc}")
        
        # Example 3: Similarity comparison
        print("\n" + "=" * 50)
        print("Example 3: Text Similarity Comparison")
        print("=" * 50)
        
        text1 = "Effective prompt engineering is crucial for AI applications."
        text2 = "Writing good prompts is essential for AI systems."
        text3 = "The cat sat on the mat."
        
        emb1 = get_embedding(client, text1)
        emb2 = get_embedding(client, text2)
        emb3 = get_embedding(client, text3)
        
        sim_1_2 = cosine_similarity(emb1, emb2)
        sim_1_3 = cosine_similarity(emb1, emb3)
        
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Text 3: {text3}")
        print(f"\nSimilarity (1 vs 2): {sim_1_2:.4f} (related texts)")
        print(f"Similarity (1 vs 3): {sim_1_3:.4f} (unrelated texts)")
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Error: {e}")
        print("Please ensure environment variables are set correctly.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
