from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generate synthetic dataset for network traffic
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_clusters_per_class=2)

# Split dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test the model
accuracy = model.score(X_test, y_test)
print(f"IDS Model Accuracy: {accuracy * 100:.2f}%")
