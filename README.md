# 🐱🐶 Cat vs Dog Image Classifier using CNN (with TensorFlow Datasets)

This project implements a Convolutional Neural Network (CNN) using **TensorFlow/Keras** to classify images as either **cats** or **dogs**. The dataset is directly loaded using `tensorflow_datasets`, so no manual downloading is required.

---

## 🧠 Model Overview

The CNN architecture includes:

- `Conv2D` layers for feature extraction
- `MaxPooling2D` layers for downsampling
- `Flatten` to convert 2D output into a vector
- `Dense` layers for classification
- A final `Dense(1, activation='sigmoid')` layer for binary prediction

---
## 🧠 Features

- Image classification between **cats** and **dogs**
- Web app built with Flask
- Upload & predict images in real-time
- TensorFlow model trained using **TFDS** (Cats vs Dogs)
---

## 🗂 Dataset

We use the **Cats vs Dogs** dataset from TensorFlow Datasets (TFDS):

```python
import tensorflow_datasets as tfds

(ds_train, ds_val), ds_info = tfds.load(
    'cats_vs_dogs',
    split=['train[:80%]', 'train[80%:]'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)
```
---
## 🌐 Google Colab

🧠 The CNN model is trained in this Colab notebook:  
👉 [Open in Google Colab](https://colab.research.google.com/drive/1-jzZAy-l_gHMvadgeTSVtPNFvVQSK2Yh)  

## 🛠 Requirements
Install the required packages:

```
pip install tensorflow tensorflow-datasets matplotlib
```
---
## ⚙️ Repository Structure

├── app.py # Flask web server\
├── static # Static files (CSS, JS, icons, images)\
   └── style.css\
   └── style.css\
├── templates # HTML templates\
 └── index.html # Upload form\
├── screenshots # Example outputs (see below) \
├── cat_dog_tfds_classifier.ipynb # CNN training notebook \
├── README.md # Project documentation  \
└── venv # Python virtual environment (excluded from Git)

---

## 🚀 How to Run Locally

### 🔧 Step 1: Create and activate a virtual environment

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```
### ⚙️ Step 2: Run the Flask app
```bash
python app.py
```

---

## 📸Screenshots 

## Home Page 
![Home Page](https://github.com/Taiyabakhan/ImageClassificationUsingCNN/blob/main/Screenshots/Screenshot%20(303).png)

## Prediction Example
![Prediction Example](https://github.com/Taiyabakhan/ImageClassificationUsingCNN/blob/main/Screenshots/Screenshot%20(304).png)
![Prediction Example](https://github.com/Taiyabakhan/ImageClassificationUsingCNN/blob/main/Screenshots/Screenshot%20(305).png)



---

## 👩‍💻 Author

**Taiyaba Khan**  
📧 khantaiyaba610@gmail.com  
🌐 [GitHub: Taiyabakhan](https://github.com/Taiyabakhan)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to fork, modify, and use it for learning or production.
