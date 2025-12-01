
# 🌸 Iris Flower Classification with Streamlit

**An interactive web application that instantly classifies Iris flowers into three species based on user-provided measurements.**

## 💡 Overview

This project is a classic machine learning demonstration, brought to life with an interactive web interface. It allows users to adjust the physical features of an Iris flower—**sepal length, sepal width, petal length, and petal width**—and receive a **real-time prediction** of its species (Setosa, Versicolor, or Virginica).

Built with **Streamlit** for the frontend and a pre-trained **Scikit-learn** model on the backend, this application is a perfect example of deploying a machine learning model for practical use.

-----

## ✨ Features

  * **Interactive Input:** Adjust four dedicated sliders to define the flower's dimensions.
  * **Real-Time Prediction:** Instant classification of the Iris species upon feature adjustment.
  * **Visual Feedback:** Displays a representative image of the predicted species.
  * **Model Confidence:** Provides prediction probabilities for all three classes, offering transparency into the model's decision.
  * **Highly Accurate:** Uses a **Random Forest Classifier** achieving $\approx 97.8\%$ accuracy.

-----

## 🔗 Live Demo

Experience the application immediately:

➡️ **[Iris Flower Classification App](https://iris-classification-tyozw8vpabhfjva2yfwyvx.streamlit.app/)**

-----

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Streamlit** | Building the clean, interactive web interface. |
| **Scikit-learn** | Machine learning model implementation (Random Forest Classifier). |
| **Pandas & NumPy** | Data manipulation and processing. |
| **Matplotlib/Seaborn** | Visualization (if applicable for model analysis or plots). |

-----

## 🚀 Installation & Usage

Follow these steps to set up and run the application locally.

### 1\. Clone the Repository

```bash
git clone https://github.com/yourusername/iris-classification.git
cd iris-classification
```

### 2\. Set Up Virtual Environment (Recommended)

It's best practice to use a virtual environment to manage dependencies:

```bash
# Create the environment
python -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate

# On Windows (Command Prompt):
# venv\Scripts\activate
```

### 3. Install Dependencies

Install all necessary libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4\. Run the Streamlit App

Start the application by executing the `app.py` file:

```bash
streamlit run app.py
```

Your default web browser will automatically open the application.

-----

## 📊 Model Details

  * **Dataset:** The classic **Iris dataset**, containing 150 samples with 4 features and 3 distinct classes (Setosa, Versicolor, Virginica).
  * **Model Type:** **Random Forest Classifier**.
  * **Performance:** Achieves approximately **$97.8\%$ accuracy** on the held-out test set.

-----

## 🧪 Example Usage

1.  Open the application via the Live Demo link or by running it locally.
2.  Adjust the four sliders (Sepal Length, Sepal Width, Petal Length, Petal Width) to your desired values.
3.  Click on the **"Classify"** button (or let the instant update occur depending on the app's design).
4.  View the **predicted Iris species** displayed prominently, along with the **confidence probabilities** for each class.

-----

## 🙏 Acknowledgements

  * **Dataset:** The foundational **Iris dataset** is sourced from the **UCI Machine Learning Repository**.
  * **Inspiration:** Tutorial resources such as *Beginner’s Guide to Building an Iris Classification App with Streamlit* were invaluable.

-----

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.. 
