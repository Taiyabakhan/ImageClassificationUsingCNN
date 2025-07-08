from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = load_model("cat_dog_model.keras")

def predict_image(img_path):
    img = Image.open(img_path).resize((128, 128)).convert("RGB")
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)  # Shape: (1, 150, 150, 3)
    print(img.shape)  # Add this
    prediction = model.predict(img)[0][0]
    return "It's a Dog 🐶" if prediction > 0.5 else "It's a Cat 🐱"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join("static", file.filename)
        file.save(filepath)
        result = predict_image(filepath)
        return render_template("index.html", prediction=result, image_path=filepath)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

