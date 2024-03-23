import streamlit as st
import tensorflow as tf
import numpy as np
# from tensorflow.keras.applications.vgg16 im


# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("TeaDiseaseModel.h5")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)
    # input_arr = np.array([input_arr])  # convert single image to batch
    # input_arr = tf.keras.applications.vgg16.preprocess_input(input_arr)
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # return index of max element


# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Main Page
if (app_mode == "Home"):
    st.header("TEA PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the TEA Plant Disease Recognition System! 🌿🔍

    Our mission is to help in identifying TEA plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art hybrid machine learning techniques for accurate tea disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Tea Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# About Project
elif (app_mode == "About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is created manually by identifying tea plant diseases  and taking picture picture. After that it was divded into class with respect to the symptoms of different disease for plant.
                This dataset consists of about ... rgb images of healthy and diseased tea leaves which is categorized into 5 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing ... test images is created later for prediction purpose.
                #### Content
                1. train (400 images)
                2. test (40 images)
                3. validation (60images)

                """)

# Prediction Page
elif (app_mode == "Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if (st.button("Show Image")):
        st.image(test_image, width=4, use_column_width=True)
    # Predict button
    if (st.button("Predict")):
        # st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        # Reading Labels
        class_name = ['ALGAL_LEAF_SPOT', 'BLISTER', 'GREY_LEAF_BLIGHT', 'HEALTHY_LEAF', 'RED_SPYDER']
        st.success(f"Model is Predicting it's a {class_name[result_index]}")