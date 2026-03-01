from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Starting training...")

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/model.pkl")

print("Training completed successfully!")