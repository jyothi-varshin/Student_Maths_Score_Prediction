from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
# Load saved objects
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
# IMPORTANT: feature order must match training (X = df.drop("math score"))
FEATURES = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course",
    "reading score",
    "writing score",
]
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = []
        for f in FEATURES:
            val = request.form.get(f)
            # numeric fields
            if f in ["reading score", "writing score"]:
                data.append(float(val))
            else:
                # encode categorical using saved encoders
                le = encoders.get(f)
                if le:
                    data.append(le.transform([val])[0])
                else:
                    data.append(float(val))
        # scale
        data_scaled = scaler.transform([data])
        # predict
        pred = model.predict(data_scaled)[0]
        return render_template(
            "index.html",
            prediction_text=f"Predicted Math Score: {round(pred, 2)}"
        )
    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)