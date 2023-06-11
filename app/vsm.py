import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def cosine_similarity_text(text1, text2):
    """
    Calculates cosine similarity between two texts.
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = np.dot(vectors[0], vectors[1].T) / (np.linalg.norm(vectors[0].toarray()) * np.linalg.norm(vectors[1].toarray()))
    return similarity

# Example usage
text1 = "This is text one."
text2 = "This is text two."
similarity = cosine_similarity_text(text1, text2)
print("Cosine similarity:", similarity)


