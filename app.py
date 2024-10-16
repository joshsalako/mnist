import streamlit as st
from tensorflow import keras
import numpy as np
from PIL import Image
import io
from streamlit_drawable_canvas import st_canvas

# Set page config
st.set_page_config(page_title="MNIST Digit Recognition", page_icon="✏️", layout="centered")

# Load the saved model
@st.cache_resource
def load_model():
    return keras.models.load_model('mnist_model.h5')

model = load_model()

# Custom CSS
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E90FF;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #32CD32;
    }
    .footer {
        font-size: 14px;
        text-align: center;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a Streamlit app
st.markdown("<p class='big-font'>MNIST Digit Recognition</p>", unsafe_allow_html=True)
st.write("Draw a digit or upload an image to see the model's prediction!")

# Add option to choose between drawing and uploading
option = st.radio("Choose input method:", ('Draw', 'Upload'))

if option == 'Draw':
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.3)",
        stroke_width=20,
        stroke_color="#FFFFFF",
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )
    
    if canvas_result.image_data is not None:
        image = Image.fromarray(canvas_result.image_data.astype('uint8'))
    else:
        image = None

else:  # Upload option
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(io.BytesIO(uploaded_file.read()))
        st.image(image, caption='Uploaded Image.', use_column_width=True)
    else:
        st.write("Please upload an image.")
        image = None

# Add a button to make a prediction
if st.button('Predict', key='predict_button'):
    if image is not None:
        # Preprocess the image
        image = image.convert('L')  # Convert to grayscale
        image = image.resize((28, 28))
        image_array = np.array(image) / 255.0  # Normalize
        image_array = image_array.reshape(1, 28, 28, 1).astype('float32')

        # Make a prediction
        with st.spinner('Predicting...'):
            prediction = model.predict(image_array)
            predicted_digit = np.argmax(prediction)

        # Display the results
        st.markdown(f"<p class='result'>Predicted Digit: {predicted_digit}</p>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.warning("Please draw or upload an image before predicting.")

st.markdown("---")
st.markdown("<div class='footer'>Created with ❤️ using Streamlit and TensorFlow<br>by <a href='https://github.com/joshsalako' target='_blank'>Joshua Salako</a></div>", unsafe_allow_html=True)
