from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

app = Flask(__name__)

# Load pre-trained model if available
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None


# 1. TRAIN endpoint
@app.route("/train", methods=["POST"])
def train_model():
    global model
    file = request.files["file"] 

    data = pd.read_csv(file)

    data["sex"] = data["sex"].map({"male": 0, "female": 1})
    data["smoker"] = data["smoker"].map({"yes": 1, "no": 0})

    # Features and target
    X = data[["age", "sex", "bmi", "children", "smoker"]]
    y = data["charges"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save model
    pickle.dump(model, open("model.pkl", "wb"))

    return jsonify({"message": "Model trained and saved successfully"})


# 2. TEST endpoint
@app.route("/test", methods=["POST"])
def test_model():
    global model
    if model is None:
        return jsonify({"error": "No model found. Train first using /train"}), 400

    file = request.files["file"]
    data = pd.read_csv(file)

    # Encode categorical
    data["sex"] = data["sex"].map({"male": 0, "female": 1})
    data["smoker"] = data["smoker"].map({"yes": 1, "no": 0})

    X = data[["age", "sex", "bmi", "children", "smoker"]]
    y = data["charges"]

    y_pred = model.predict(X)

    score = model.score(X, y)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)

    return jsonify({"mse":mse,"mae":mae, "r2_score": score})


# 3. PREDICT endpoint
@app.route("/predict", methods=["POST"])
def predict():
    global model
    if model is None:
        return jsonify({"error": "No model found. Train first using /train"}), 400

    data = request.get_json()

    age = data["age"]
    sex = 0 if data["sex"].lower() == "male" else 1
    bmi = data["bmi"]
    children = data["children"]
    smoker = 1 if data["smoker"].lower() == "yes" else 0

    x_test = [[age, sex, bmi, children, smoker]]
    prediction = round(model.predict(x_test)[0], 2)

    return jsonify({"predicted_premium": prediction})


if __name__ == "__main__":
    app.run(debug=True)