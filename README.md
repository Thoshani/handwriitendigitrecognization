# handwriitendigitrecognization
#  Handwritten Digit Recognizer

This is a simple Tkinter-based GUI app that recognizes handwritten digits using a trained CNN model on the MNIST dataset.
![image](https://github.com/user-attachments/assets/b9e3ea5a-839c-4da9-8bfe-452c1a54635d)

## Features
- Draw a digit on canvas
- Press "Predict" to classify
- Clear button to redraw
- Simple UI with accurate predictions

##  Requirements
Install dependencies:
pip install -r requirements.txt

## ▶ How to Run
Make sure `digit_model.h5` is in the same folder.

Run the app:
python digit_recognizer_app.py

markdown
Copy
Edit

## Model
The model is trained on the MNIST dataset using TensorFlow and saved as `digit_model.h5`.


## Built With
- Python
- Tkinter
- TensorFlow
- PIL (Pillow)
