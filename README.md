Iris Flower Classification with Streamlit

An interactive web application that classifies Iris flowers into three species—Setosa, Versicolor, and Virginica—based on user-input features: sepal length, sepal width, petal length, and petal width.

Built using Streamlit and a pre-trained Random Forest model, this app provides real-time predictions, probabilities, and visual feedback.

🔗 Live Demo: https://iris-classification-tyozw8vpabhfjva2yfwyvx.streamlit.app/


---

✨ Features

✅ Interactive Input – Adjust sliders for sepal & petal dimensions
✅ Real-Time Prediction – Instant classification of Iris species
✅ Visual Feedback – Displays images of the predicted species
✅ Model Confidence – Shows prediction probabilities for each class


---

🛠️ Technologies Used

🎨 Streamlit – Interactive web app framework

🤖 Scikit-learn – Machine learning model (Random Forest Classifier)

📊 Pandas & NumPy – Data processing & manipulation

📈 Matplotlib/Seaborn – Data visualization (optional)



---

📥 Installation & Usage

# 1️⃣ Clone the Repository
git clone https://github.com/yourusername/iris-classification.git
cd iris-classification

# 2️⃣ (Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit App
streamlit run app.py

👉 This will open the app in your default web browser.


---

📊 Model Details

📂 Dataset: Iris dataset (150 samples, 3 species)

🌲 Model: Random Forest Classifier

🎯 Accuracy: ~97.8% on test set



---

🧪 Example Usage

1. Adjust the sliders for sepal and petal dimensions


2. Click "Classify"


3. View the predicted Iris species 🌺 along with confidence probabilities 📊




---

📚 Acknowledgements

📑 Dataset: UCI Machine Learning Repository – Iris Dataset

📝 Tutorial Inspiration: Beginner’s Guide to Building an Iris Classification App with Streamlit



---

📄 License

📜 This project is licensed under the MIT License – see the LICENSE file for details.

