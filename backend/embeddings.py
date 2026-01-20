import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import TypedDict

class EmbeddingResult(TypedDict):
    embedding: list[float]
    model: str
    total_tokens: int
    cost: float
    price_per_1M: float

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), max_retries=5)

def get_embeddings(text: str, embedding_model: str = "text-embedding-3-small") -> EmbeddingResult:
    """
    Generate embeddings for the given text using OpenAI's embedding API.
    Args:
        text (str): The input text to generate embeddings for.
        embedding_model (str, optional): The embedding model to use. 
            Defaults to "text-embedding-3-small".
    Returns:
        EmbeddingResult: A dictionary containing:
            - embedding (list): The generated embedding vector.
            - model (str): The name of the embedding model used.
            - total_tokens (int): Total number of tokens processed.
            - cost (float): The cost of the API call in USD.
            - price_per_1M (float): The price per 1M tokens for the model.
    Raises:
        ValueError: If the specified embedding_model is not recognized or 
            not in the model_prices dictionary.
    """

    # Per 1M tokens
    model_prices = {
        "text-embedding-3-small": 0.02
    }

    response = client.embeddings.create(
        input = text,
        model = embedding_model
    )

    # No output tokens generated for embedding models
    total_tokens = response.usage.total_tokens
    if embedding_model not in model_prices:
        raise ValueError(f"Unkown embedding model: {embedding_model}")
    cost = (total_tokens / 1_000_000) * model_prices[embedding_model]

    return {
        "embedding": response.data[0].embedding,
        "model": embedding_model,
        "total_tokens": total_tokens,
        "cost": cost,
        "price_per_1M": model_prices[embedding_model]
    }

# print(response.data[0].embedding)
