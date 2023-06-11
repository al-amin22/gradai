import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer



text1 = "Ini adalah teks pertama"
text2 = "Ini adalah teks kedua"


vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2])

model = LinearRegression()
model.fit(vectors[0], vectors[1])

similarity = cosine_similarity(vectors[0], vectors[1])


print('similarity')