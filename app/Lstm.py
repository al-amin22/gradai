import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.layers.embeddings import Embedding
from keras.preprocessing.sequence import pad_sequences
from keras.optimizers import Adam

# Input data
text1 = "Machine learning is a subset of artificial intelligence that involves training algorithms to make predictions or decisions based on data."
text2 = "Artificial intelligence is a broader concept that involves the development of intelligent machines that can perform tasks without human intervention."

# Tokenize the input texts
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text1, text2])
sequences = tokenizer.texts_to_sequences([text1, text2])

# Pad sequences to have same length
max_len = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_len)

# Define LSTM model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=50, input_length=max_len))
model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(padded_sequences, np.array([1, 0]), epochs=50, batch_size=1, verbose=0)

# Evaluate the model
similarity = model.predict(pad_sequences(tokenizer.texts_to_sequences([text1, text2]), maxlen=max_len))
print("Similarity:", similarity)
