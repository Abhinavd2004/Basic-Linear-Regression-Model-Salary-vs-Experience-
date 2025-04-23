from flask import Flask, request, jsonify, render_template
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("linear_regression_data.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# 3) Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        exp = float(data.get("experience", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid experience value"}), 400

    pred = model.predict([[exp]])[0]
    return jsonify({"predicted_salary": round(float(pred), 2)})


if __name__ == "__main__":
    app.run(debug=True)

