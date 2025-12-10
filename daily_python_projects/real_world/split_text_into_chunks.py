import numpy as np

def split_text_into_chunks(text, max_len=200):
    """
    Splits text into chunks of max_len characters without breaking words.
    """
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        # Check if adding this word exceeds the max length
        if len(current_chunk) + len(word) + 1 <= max_len:
            current_chunk += (" " if current_chunk else "") + word
        else:
            chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def generate_dummy_embeddings(chunks, dim=768):
    """
    Generates random embeddings for each chunk.
    """
    embeddings = [np.random.rand(dim) for _ in chunks]
    return embeddings


if __name__ == "__main__":
    text = (
        "You are given a block of text and asked to prepare it for a "
        "Retrieval-Augmented Generation (RAG) pipeline. The goal is to split "
        "the text into smaller chunks that can be indexed, while also ensuring "
        "no words are cut in the process. Each chunk will be associated with "
        "a vector embedding for semantic search."
    )

    # Step 1: Split into chunks
    chunks = split_text_into_chunks(text, max_len=200)
    print("Text Chunks:")
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {chunk}\n")

    # Step 2: Generate dummy embeddings
    embeddings = generate_dummy_embeddings(chunks, dim=768)
    print("Embeddings shape per chunk:", embeddings[0].shape)
