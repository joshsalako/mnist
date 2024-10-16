# MNIST Digit Recognition App

This Streamlit app uses a trained neural network to recognize handwritten digits from the MNIST dataset. Users can either draw a digit or upload an image of a digit, and the app will predict which digit it is.

## Features

- Draw a digit using an interactive canvas
- Upload an image of a digit
- Real-time prediction of the drawn or uploaded digit
- User-friendly interface with Streamlit

## Installation

1. Clone this repository:   ```
   git clone https://github.com/yourusername/mnist-digit-recognition.git
   cd mnist-digit-recognition   ```

2. Install the required packages:   ```
   pip install -r requirements.txt   ```

3. Run the Streamlit app:   ```
   streamlit run app.py   ```

## Usage

1. Choose between drawing a digit or uploading an image.
2. If drawing, use your mouse or touchpad to draw a digit on the canvas.
3. If uploading, select an image file of a handwritten digit.
4. Click the "Predict" button to see the model's prediction.

## Model

The app uses a pre-trained convolutional neural network (CNN) model saved as 'mnist_model.h5'. The model was trained on the MNIST dataset of handwritten digits.

## Dependencies

- streamlit
- tensorflow
- numpy
- pillow
- streamlit-drawable-canvas

For a complete list of dependencies, see `requirements.txt`.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/mnist-digit-recognition/issues) if you want to contribute.

## Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
