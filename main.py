import streamlit as st
import tensorflow as tf
import numpy as np
# from tensorflow.keras.models import load
# from tensorflow.keras.applications.vgg16 im


# Tensorflow Model Prediction
def model_prediction(x,test_image):
    model = tf.keras.models.load_model(x)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)
    predictions = model.predict(input_arr)
    # return predictions  #  new checking
    return np.argmax(predictions)
    # return index of max element
# input_arr = np.array([input_arr])  # convert single image to batch
    # input_arr = tf.keras.applications.vgg16.preprocess_input(input_arr)


# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Rice Disease Recognition","Sugracane Disease Recognition","Tea Disease Recognition"])

# Main Page
if (app_mode == "Home"):
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.png"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍

    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

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
                This dataset is created manually and also with the help of open source data by identifying pant diseases(rice, sugarcane,tea) and taking picture. After that it was divded into class with respect to the symptoms of different disease for plant.
                This dataset consists of about rgb images of healthy and diseased leaves which is categorized into different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing test images is created later for prediction purpose.
                #### Content
                1. train (5000 images)
                2. test (1000 images)
                3. validation (800images)

                """)
    image_path = "about_page.png"
    st.image(image_path, use_column_width=True)

    st.markdown("""
                            ### Rice Disease
                            
                            
                            ### Rice - Bacterial Leaf Blight
                """)
    image_path = "DiseaseImages/Rice/Bacterial_Leaf_Blight.JPG"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                        #### Causes of Bacterial Leaf Blight in Rice

                        1. **Bacterium**:
                           - Caused by the bacterium *Xanthomonas oryzae* pv. *oryzae*.
                        
                        2. **Weather Conditions**:
                           - Warm and humid conditions favor the disease.
                        
                        3. **Irrigation Practices**:
                           - Poor water management, such as flooding and waterlogged conditions, can facilitate the spread.
                        
                        4. **Infected Seeds**:
                           - Using seeds from infected plants can introduce the bacteria to new fields.
                        
                        5. **Wounds on Plants**:
                           - Injuries from farming activities, insect bites, or storms can provide entry points for the bacteria.
                        
                        #### Remedies for Bacterial Leaf Blight in Rice
                        
                        1. **Resistant Varieties**:
                           - Planting rice varieties that are resistant or tolerant to bacterial leaf blight to reduce disease incidence.
                        
                        2. **Seed Treatment**:
                           - Treating seeds with appropriate bactericides before planting to reduce the risk of seedborne infection.
                        
                        3. **Water Management**:
                           - Avoid over-irrigation and ensure proper drainage to prevent waterlogged conditions.
                        
                        4. **Field Sanitation**:
                           - Remove and destroy infected plant residues and weeds that may harbor the bacteria.
                        
                        5. **Balanced Fertilization**:
                           - Avoid excessive nitrogen fertilization which can promote lush growth and make plants more susceptible.
                        """)
    st.markdown("""
                                 ### Rice - Brown Spot
                    """)
    image_path = "DiseaseImages/Rice/Brown_Spot.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("""                                              
                        #### Causes of Rice Brown Spot
                        
                        1. Fungus:
                           - Caused by the fungus Bipolaris oryzae (formerly Helminthosporium oryzae).
                        
                        2. Weather Conditions:
                           - Favorable conditions include warm temperatures (20-30°C), high humidity, and frequent rain.
                        
                        3. Nutrient Deficiency:
                           - Poor soil fertility, particularly nitrogen and potassium deficiencies, can make rice plants more susceptible.
                        
                        4. Seedborne Infection:
                           - Infected seeds can introduce the fungus into new fields.
                        
                        5. Poor Field Sanitation:
                           - Crop residues and weeds can harbor the fungus and facilitate its spread.                        
                                              
                        #### Remedies for Rice Brown Spot
                        
                        1. **Use of Resistant Varieties**:
                           - Planting rice varieties that are resistant or tolerant to brown spot can significantly reduce disease incidence.
                        
                        2. **Seed Treatment**:
                           - Treat seeds with appropriate fungicides to kill any seedborne fungi before planting.
                        
                        3. **Nutrient Management**:
                           - Ensure balanced fertilization, particularly with adequate nitrogen and potassium, to maintain healthy plant growth.
                        
                        4. **Field Sanitation**:
                           - Remove and destroy infected plant debris and weeds to reduce sources of inoculum.
                        
                        5. **Crop Rotation**:
                           - Practice crop rotation with non-host crops to disrupt the life cycle of the fungus.                       
                        
                        """)
    st.markdown("""
                                     ### Rice - Leaf Smut
                        """)
    image_path = "DiseaseImages/Rice/Leaf_Smut.JPG"
    st.image(image_path, use_column_width=True)

    st.markdown("""
                            #### Causes of Rice Leaf Smut

                            1. **Fungus**:
                               - Caused by the fungus *Entyloma oryzae*.
                            
                            2. **Weather Conditions**:
                               - Warm and humid conditions favor the development and spread of the disease.
                            
                            3. **Infected Seeds**:
                               - Using infected seeds can introduce the fungus to new fields.
                            
                            4. **Soil and Plant Debris**:
                               - The fungus can survive in soil and plant debris, acting as a source of inoculum.
                            
                            5. **Susceptible Varieties**:
                               - Planting rice varieties that are more susceptible to the disease.
                            
                            
                            
                            ### Remedies for Rice Leaf Smut
                            
                            1. **Use of Resistant Varieties**:
                               - Plant rice varieties that are resistant or tolerant to leaf smut to reduce disease incidence.
                            
                            2. **Seed Treatment**:
                               - Treat seeds with appropriate fungicides to eliminate any seedborne fungi before planting.
                            
                            3. **Field Sanitation**:
                               - Remove and destroy infected plant debris and weeds to reduce sources of inoculum.
                            
                            4. **Crop Rotation**:
                               - Practice crop rotation with non-host crops to break the life cycle of the fungus.
                            
                            5. **Water Management**:
                               - Ensure proper irrigation and drainage to avoid waterlogged conditions.
                            
                            
                            """)

    st.markdown("""
                    ### Sugarcane Diease
                    
                    """)
    
    st.markdown("""
                                 ### Sugarcane - Mosaic
                    """)
    image_path = "DiseaseImages/sugarcane/Mosaic.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                            #### Causes of Sugarcane Mosaic Disease

                            1. **Virus**:
                               - Caused by Sugarcane mosaic virus (SCMV) and related viruses such as Maize dwarf mosaic virus (MDMV) and Sorghum mosaic virus (SrMV).
                            
                            2. **Insect Vectors**:
                               - Primarily spread by aphids, particularly the green peach aphid (*Myzus persicae*) and corn leaf aphid (*Rhopalosiphum maidis*).
                            
                            3. **Infected Plant Material**:
                               - Using infected cuttings or plant material for propagation introduces the virus to new fields.
                            
                            4. **Mechanical Transmission**:
                               - Transmitted through contaminated tools, machinery, and hands during cultivation.
                            
                            5. **Alternate Hosts**:
                               - Presence of alternate hosts, such as maize, sorghum, and certain grasses, which can harbor the virus and facilitate its spread.
                            
                            #### Remedies for Sugarcane Mosaic Disease
                            
                            1. **Resistant Varieties**:
                               - Planting sugarcane varieties that are resistant or tolerant to mosaic disease to reduce infection rates.
                            
                            2. **Aphid Control**:
                               - Implementing integrated pest management (IPM) strategies, including the use of insecticides, natural predators, and biological control agents to manage aphid populations.
                            
                            3. **Certified Plant Material**:
                               - Using certified, disease-free cuttings and planting material to prevent the introduction of the virus.
                            
                            4. **Field Sanitation**:
                               - Removing and destroying infected plants and weeds to reduce sources of virus inoculum.
                            
                            5. **Tool Sanitation**:
                               - Regularly disinfecting tools, machinery, and hands to prevent mechanical transmission of the virus.

                            """)
    st.markdown("""
                                 ### Sugarcane - RedRot
                    """)
    image_path = "DiseaseImages/sugarcane/RedRot.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                            #### Causes of Sugarcane Red Rot Disease

                            1. **Fungus**:
                               - Caused by the fungus *Colletotrichum falcatum* (also known as *Glomerella tucumanensis*).
                            
                            2. **Infected Setts**:
                               - Using infected setts (cuttings) for planting can introduce the fungus to new fields.
                            
                            3. **Poor Field Drainage**:
                               - Waterlogged conditions and poor drainage can facilitate the growth and spread of the fungus.
                            
                            4. **High Humidity and Temperature**:
                               - Warm (25-30°C) and humid conditions favor the development of the disease.
                            
                            5. **Mechanical Injury**:
                               - Injuries to the plant from cultivation practices, pests, or environmental factors provide entry points for the fungus.
                            
                            ### Remedies for Sugarcane Red Rot Disease
                            
                            1. **Resistant Varieties**:
                               - Planting sugarcane varieties that are resistant or tolerant to red rot to minimize disease incidence.
                            
                            2. **Healthy Planting Material**:
                               - Using disease-free setts treated with fungicides before planting to prevent infection.
                            
                            3. **Field Sanitation**:
                               - Removing and destroying infected plant debris and maintaining weed-free fields to reduce sources of inoculum.
                            
                            4. **Improved Drainage**:
                               - Ensuring proper field drainage to avoid waterlogging and reduce favorable conditions for fungal growth.
                            
                            5. **Crop Rotation**:
                               - Practicing crop rotation with non-host crops to break the life cycle of the fungus and reduce soil-borne inoculum.

                            """)
    st.markdown("""
                                 ### Sugarcane - Rust
                    """)
    image_path = "DiseaseImages/sugarcane/Rust.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                            #### Causes of Sugarcane Rust Disease

                            1. **Fungus**:
                               - Caused by the fungus *Puccinia melanocephala* (Brown Rust) or *Puccinia kuehnii* (Orange Rust).
                            
                            2. **Weather Conditions**:
                               - Warm and humid conditions favor the development and spread of rust diseases.
                            
                            3. **Infected Plant Material**:
                               - Using infected cuttings or plant material for propagation introduces the fungus to new fields.
                            
                            4. **Wind and Rain**:
                               - Spores are spread by wind and rain, facilitating rapid dissemination across fields.
                            
                            5. **Dense Planting**:
                               - High plant density creates a microenvironment conducive to fungal growth and spore dissemination.
                            
                            #### Remedies for Sugarcane Rust Disease
                            
                            1. **Resistant Varieties**:
                               - Planting sugarcane varieties that are resistant or tolerant to rust diseases to reduce infection rates.
                            
                            2. **Healthy Planting Material**:
                               - Using certified, disease-free cuttings and planting material to prevent the introduction of the fungus.
                            
                            3. **Field Sanitation**:
                               - Removing and destroying infected plant debris and maintaining clean fields to reduce sources of inoculum.
                            
                            4. **Fungicide Application**:
                               - Applying recommended fungicides as a preventive measure or at early signs of infection to control the spread.
                            
                            5. **Proper Plant Spacing**:
                               - Maintaining appropriate plant spacing to improve air circulation and reduce humidity, which can help prevent fungal growth.

                            """)
    st.markdown("""
                                 ### Sugarcane - Yellow
                    """)
    image_path = "DiseaseImages/sugarcane/Yellow.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                             #### Causes of Sugarcane Yellow Disease

                            1. **Phytoplasma**:
                               - Caused by phytoplasmas, which are specialized bacteria lacking a cell wall.
                            
                            2. **Insect Vectors**:
                               - Transmitted by sap-sucking insects, particularly leafhoppers.
                            
                            3. **Infected Plant Material**:
                               - Using infected cuttings or planting material can introduce the phytoplasma to new fields.
                            
                            4. **Environmental Stress**:
                               - Conditions such as drought or nutrient deficiencies can exacerbate the susceptibility of plants to the disease.
                            
                            5. **Alternate Hosts**:
                               - Presence of alternate host plants that can harbor the phytoplasma and facilitate its spread.
                            
                            ### Remedies for Sugarcane Yellow Disease
                            
                            1. **Resistant Varieties**:
                               - Planting sugarcane varieties that are resistant or tolerant to yellow disease to reduce infection rates.
                            
                            2. **Insect Vector Control**:
                               - Implementing integrated pest management (IPM) strategies, including the use of insecticides and natural predators, to control leafhopper populations.
                            
                            3. **Certified Plant Material**:
                               - Using certified, disease-free cuttings and planting material to prevent the introduction of the phytoplasma.
                            
                            4. **Field Sanitation**:
                               - Removing and destroying infected plants and controlling weeds to reduce sources of phytoplasma and its vectors.
                            
                            5. **Balanced Nutrient Management**:
                               - Ensuring proper fertilization and irrigation to maintain healthy plant growth and reduce susceptibility to the disease.
                               """)
    
    st.markdown("""
                    #### Tea Disease
                    
                    """)

    st.markdown("""
                        #### Tea -Algal Leaf

                        """)
    image_path = "DiseaseImages/Tea/AlgalLeaf.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                        #### Causes of Tea Algal Leaf Disease

                        1. **Alga**:
                           - Caused by the alga *Cephaleuros virescens*.
                        
                        2. **Weather Conditions**:
                           - Warm, humid, and wet conditions favor the development and spread of the disease.
                        
                        3. **Infected Plant Material**:
                           - Using infected cuttings or propagation material can introduce the alga to new areas.
                        
                        4. **Dense Planting**:
                           - High plant density creates a microenvironment conducive to algal growth and spread.
                        
                        5. **Poor Air Circulation**:
                           - Insufficient air circulation in dense canopies promotes moisture retention, facilitating algal proliferation.
                        
                        ### Remedies for Tea Algal Leaf Disease
                        
                        1. **Resistant Varieties**:
                           - Planting tea varieties that are resistant or tolerant to algal leaf disease to reduce infection rates.
                        
                        2. **Proper Plant Spacing**:
                           - Maintaining appropriate plant spacing to improve air circulation and reduce humidity, which can help prevent algal growth.
                        
                        3. **Field Sanitation**:
                           - Removing and destroying infected leaves and plant debris to reduce sources of algal inoculum.
                        
                        4. **Fungicide Application**:
                           - Applying recommended fungicides or algicides as a preventive measure or at early signs of infection to control the spread of the alga.
                        
                        5. **Improved Drainage**:
                           - Ensuring proper field drainage to avoid waterlogged conditions, which can create favorable conditions for the alga.

                            """)
    st.markdown("""
                        #### Tea - Blister

                        """)
    image_path = "DiseaseImages/Tea/Blister.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                        #### Causes of Tea Blister Disease

                        1. **Fungi**:
                           - Caused by fungal pathogens such as *Exobasidium vexans*.
                        
                        2. **Weather Conditions**:
                           - Cool, moist, and foggy weather conditions favor the development and spread of the fungus.
                        
                        3. **Infected Plant Material**:
                           - Using infected cuttings or planting material can introduce the pathogen to new tea plantations.
                        
                        4. **Mechanical Injury**:
                           - Wounds caused by pruning, harvesting, or environmental factors provide entry points for fungal infection.
                        
                        5. **High Humidity**:
                           - Prolonged periods of high humidity create an ideal environment for the fungus to thrive and infect the tea plants.
                        
                        #### Remedies for  Tea Blister Disease
                        
                        1. **Resistant Varieties**:
                           - Planting tea varieties that are resistant or tolerant to tea blister disease to reduce the incidence of infection.
                        
                        2. **Proper Plant Hygiene**:
                           - Regularly removing and destroying infected leaves and branches to lower the amount of fungal inoculum in the plantation.
                        
                        3. **Fungicide Application**:
                           - Applying fungicides as per recommended guidelines, especially during conditions favorable for disease development, to control the spread of the fungus.
                        
                        4. **Improved Air Circulation**:
                           - Ensuring proper plant spacing and pruning to enhance air circulation and reduce moisture levels around the tea plants.
                        
                        5. **Soil Management**:
                           - Maintaining well-draining soil and avoiding prolonged periods of soil moisture to reduce the risk of fungal growth and infection.

                            """)
    st.markdown("""
                        #### Tea - Grey Leaf Blight

                        """)
    image_path = "DiseaseImages/Tea/GreyLeafBlight.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                        #### Causes of Tea Grey Leaf Blight Disease

                        1. **Fungi**:
                           - Caused by fungal pathogens such as *Pestalotiopsis* ssp.
                        
                        2. **Weather Conditions**:
                           - Warm and humid weather conditions facilitate the growth and spread of the fungus.
                        
                        3. **Infected Plant Material**:
                           - Using infected cuttings or planting material can introduce the fungus to new areas.
                        
                        4. **Mechanical Injury**:
                           - Wounds caused by pruning, harvesting, or environmental factors provide entry points for fungal infection.
                        
                        5. **Poor Air Circulation**:
                           - Dense canopies and overcrowded planting conditions hinder air circulation, promoting fungal proliferation.
                        
                        #### Remedies for Tea Grey Leaf Blight Disease
                        
                        1. **Resistant Varieties**:
                           - Planting tea varieties that are resistant or tolerant to bird eye spot disease to minimize disease incidence.
                        
                        2. **Pruning and Plant Hygiene**:
                           - Pruning affected branches and removing fallen leaves to reduce fungal inoculum and prevent disease spread.
                        
                        3. **Fungicide Application**:
                           - Applying fungicides at recommended intervals, especially during periods of high disease pressure, to control fungal spread.
                        
                        4. **Improved Air Circulation**:
                           - Thinning out dense canopies and ensuring proper plant spacing to enhance airflow and reduce humidity.
                        
                        5. **Soil Management**:
                           - Maintaining well-draining soil and avoiding waterlogging to discourage fungal growth and spread.

                            """)
    st.markdown("""
                        #### Tea - Red Spider

                        """)
    image_path = "DiseaseImages/Tea/RedSpyder.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
                        #### Causes of Red Spider Mite Disease in Tea

                        1. **Mites**:
                           - Caused by red spider mites, primarily *Oligonychus coffeae*.
                        
                        2. **Weather Conditions**:
                           - Hot and dry weather conditions favor the proliferation of red spider mites.
                        
                        3. **Infected Plant Material**:
                           - Using infested cuttings or planting material can introduce red spider mites to new tea plantations.
                        
                        4. **Poor Plant Healthy**:
                           - Weak or stressed plants are more susceptible to red spider mite infestations.
                        
                        5. **Lack of Natural Predators**:
                           - Absence of natural predators that help control red spider mite populations..
                        
                        #### Remedies for Red Spider Mite Disease in Tea
                        
                        1. **Resistant Varieties**:
                           - Planting tea varieties that are less susceptible to red spider mite infestations to minimize damage.
                        
                        2. **Proper Plant Hygiene**:
                           - Regularly inspecting plants and removing infested leaves or branches to reduce mite populations.
                        
                        3. **Acaricide Application**:
                           - Applying acaricides at recommended intervals, especially during peak infestation periods, to control mite populations.
                        
                        4. **Improved Water Management**:
                           - Maintaining adequate soil moisture through proper irrigation practices to keep plants healthy and reduce stress.
                        
                        5. **Biological Control**:
                           - Encouraging or introducing natural predators, such as predatory mites and insects, to keep red spider mite populations in check.

                            """)



# Prediction Page

#Page 1
elif (app_mode == "Rice Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if (st.button("Show Image")):
        st.image(test_image, width=4, use_column_width=True)
    # Predict button
    if (st.button("Predict")):
        # st.snow()
        st.write("Our Prediction")
        result_index = model_prediction("HybridRiceDiseaseModel.h5",test_image)
        # Reading Labels             
        class_name = ['Bacterial Leaf Blight','Brown Spot','Leaf Smut']
        st.success(f"Model is Predicting it's a {class_name[result_index]}. Please checkout for causes and remedies on About Page")

#Page 2
elif (app_mode == "Sugracane Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if (st.button("Show Image")):
        st.image(test_image, width=4, use_column_width=True)
    # Predict button
    if (st.button("Predict")):
        # st.snow()
        st.write("Our Prediction")
        result_index = model_prediction("SugarcaneDiseaseDetectionmodel.keras",test_image)
        # Reading Labels
        class_name = ['Healthy Sugarcane', 'Mosaic Sugarcane', 'RedRotSugarcane', 'Rust Sugarcane', 'Yellow Sugarcane']
        if(result_index==0):
            st.success(f"Model is Predicting it's a {class_name[result_index]}.")
        else:
            st.success(f"Model is Predicting it's a {class_name[result_index]}. Please checkout for causes and remedies on About Page")

#Page 3
elif (app_mode == "Tea Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if (st.button("Show Image")):
        st.image(test_image, width=4, use_column_width=True)
    # Predict button
    if (st.button("Predict")):
        # st.snow()
        st.write("Our Prediction")
        result_index = model_prediction("Models.pb",test_image)

        class_name = ['ALGAL_LEAF_SPOT', 'BLISTER', 'GREY_LEAF_BLIGHT', 'HEALTHY_LEAF', 'RED_SPYDER']
        if (result_index == 3):
            st.success(f"Model is Predicting it's a {class_name[result_index]}.")
        else:
            st.success(
                f"Model is Predicting it's a {class_name[result_index]}. Please checkout for causes and remedies on About Page")

