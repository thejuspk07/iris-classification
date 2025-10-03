import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":red[IRIS FLOWER CLASSIFICATION 🌸]")

    # Optional image
    try:
        img = Image.open("iris.png")  # keep iris.png in same folder
        st.image(img, width=600)
    except:
        st.info("🌼 Add 'iris.png' in same folder to show an image.")

    # Inputs
    sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, format="%.2f")
    sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, format="%.2f")
    petal_length = st.number_input('Petal Length (cm)', min_value=0.0, format="%.2f")
    petal_width = st.number_input('Petal Width (cm)', min_value=0.0, format="%.2f")

    # Feature list
    features = [sepal_length, sepal_width, petal_length, petal_width]

    # Load model & scaler
    model = pickle.load(open("model_knn.sav1", "rb"))
    scaler = pickle.load(open("scaler_knn.sav1", "rb"))

    # Prediction
    label_map = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

    if st.button("🔮 PREDICT"):
        prediction = model.predict(scaler.transform([features]))
        flower = label_map[int(prediction[0])]
        st.success(f"🌼 Predicted Flower: **{flower}**")
        st.balloons()




if __name__ == "__main__":
    main()
