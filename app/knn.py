import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

# Contoh data teks
data = pd.DataFrame({
    'teks': ['saya suka makan', 'saya senang bermain', 'anda suka tidur', 'anda senang berolahraga']
})

# Proses vektorisasi teks menggunakan TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['teks'])

# Menentukan label untuk setiap data teks
y = np.array([0, 1, 0, 1])

# Membuat model KNN dengan k=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# Contoh dua teks yang akan dibandingkan
teks1 = 'saya suka makan'
teks2 = 'saya suka minum'

# Vektorisasi teks yang akan dibandingkan
X_test = vectorizer.transform([teks1, teks2])

# Memprediksi label untuk teks yang akan dibandingkan
y_pred = knn.predict(X_test)

# Menampilkan hasil prediksi
for i in range(len(X_test)):
    print('Teks:', [teks1, teks2][i])
    print('Label:', ['sama', 'tidak sama'][y_pred[i]])
