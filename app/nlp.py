
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def cosine_sim(text1, text2):
    corpus = [text1, text2]
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(corpus)
    similarity = cosine_similarity(cv_matrix)
    return similarity[0][1]