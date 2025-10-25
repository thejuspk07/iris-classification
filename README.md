🌸 Iris Flower Classification with Streamlit 🌿

An interactive web application that classifies Iris flowers into one of three species — Setosa, Versicolor, or Virginica — based on their key physical measurements.
This app uses a pre-trained machine learning model and provides real-time predictions with visual feedback.

🔗 Live Demo: Iris Classification App

✨ Features

🎚️ Interactive Input: Easily adjust sliders to modify sepal length, sepal width, petal length, and petal width.

⚡ Real-Time Prediction: Instantly get the predicted Iris species.

🌼 Visual Feedback: Displays an image of the predicted species for easy identification.

📈 Model Confidence: Shows prediction probabilities for all three classes.

🛠️ Technologies & Model Details
Technology	Purpose
Streamlit	Build the interactive web interface and handle deployment.
Scikit-learn	Machine learning model implementation and training.
Pandas & NumPy	Data manipulation and numerical processing.
Matplotlib / Seaborn	Data visualization and exploratory analysis.
📊 Machine Learning Model

Dataset: Classic Iris dataset (150 samples, 3 classes) from the UCI Machine Learning Repository.

Model: Random Forest Classifier.

Accuracy: Achieves approximately 97.8% accuracy on the test set.

🚀 Installation & Local Usage

Follow these steps to set up and run the application on your local machine:

1️⃣ Clone the Repository
git clone https://github.com/yourusername/iris-classification.git
cd iris-classification

2️⃣ Set Up a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

python -m venv venv
source venv/bin/activate


On Windows:

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app.py


This will automatically open the app in your default web browser.

🧪 Example Usage

Open the application in your browser (via the Live Demo link or by running it locally).

Use the sliders on the sidebar to input new sepal and petal measurements.

View the predicted Iris species displayed prominently.

Check the confidence probabilities for each class provided by the model.

📚 Acknowledgements

Dataset: Iris dataset
 from the UCI Machine Learning Repository.

Inspiration: Beginner’s Guide to Building an Iris Classification App with Streamlit.

📄 License

This project is licensed under the MIT License — see the LICENSE
 file for details
