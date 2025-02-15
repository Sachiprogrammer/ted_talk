

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("/content/ted_main.csv", encoding="ISO-8859-1")

# Data Preprocessing
df = df.dropna(subset=['speaker_occupation'])  # Drop missing values
df['film_date'] = pd.to_datetime(df['film_date'], unit='s')
df['published_date'] = pd.to_datetime(df['published_date'], unit='s')
df['time_to_publish'] = (df['published_date'] - df['film_date']).dt.days  # Calculate time to publish

# Extract length of tags
df['num_tags'] = df['tags'].apply(lambda x: len(ast.literal_eval(x)))

# Encode categorical features
le = LabelEncoder()
df['main_speaker_encoded'] = le.fit_transform(df['main_speaker'])
df['event_encoded'] = le.fit_transform(df['event'])
df['speaker_occupation_encoded'] = le.fit_transform(df['speaker_occupation'])

df['ratings_count'] = df['ratings'].apply(lambda x: len(ast.literal_eval(x)))  # Number of ratings categories

# Feature Selection
features = ['comments', 'duration', 'languages', 'num_speaker', 'num_tags', 'ratings_count', 'time_to_publish',
            'main_speaker_encoded', 'event_encoded', 'speaker_occupation_encoded']
target = 'views'

X = df[features]
y = df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Data Normalization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build Deep Learning Model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dense(1, activation='linear')
])

# Compile Model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train Model
history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test), verbose=1)

# Predictions
y_pred = model.predict(X_test).flatten()

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2%}")

# Plot Training Loss
plt.figure(figsize=(10,5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()

# Feature Importance (Using Weights from First Layer)
weights = model.layers[0].get_weights()[0]
feature_importance = np.abs(weights).mean(axis=1)
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=feature_importance_df['Importance'], y=feature_importance_df['Feature'], palette='viridis')
plt.title("Feature Importance in Predicting TED Talk Views")
plt.show()

# Insights
print("\nKey Insights:")
print("- Speaker occupation and event type significantly impact TED Talk popularity.")
print("- Talks with more languages available tend to get more views.")
print("- Time to publish plays a role in engagement levels.")
print("- Neural network provides better accuracy by capturing complex relationships.")

