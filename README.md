# iris-classification
🌸 Iris Flower Classification with Streamlit

This is an interactive web application that classifies Iris flowers into three species—Setosa, Versicolor, and Virginica—based on user-input features: sepal length, sepal width, petal length, and petal width. Built using Streamlit and a pre-trained machine learning model, this app provides real-time predictions and visual feedback.

🔗 Live Demo: https://iris-classification-tyozw8vpabhfjva2yfwyvx.streamlit.app/

📌 Features

Interactive Input: Adjust sliders for sepal and petal dimensions.

Real-Time Prediction: Instant classification of Iris species.

Visual Feedback: Displays images of the predicted species.

Model Confidence: Shows prediction probabilities for each class.

🛠️ Technologies Used

Streamlit: For building the interactive web interface.

Scikit-learn: For machine learning model implementation.

Pandas & NumPy: For data manipulation and processing.

Matplotlib/Seaborn: For data visualization (if applicable).

📥 Installation & Usage
1. Clone the Repository
git clone https://github.com/yourusername/iris-classification.git
cd iris-classification

2. Set Up Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py


This will open the app in your default web browser.

📊 Model Details

Dataset: Iris dataset containing 150 samples with 3 classes.

Model: Trained using a Random Forest Classifier.

Accuracy: Achieves approximately 97.8% accuracy on the test set.

🧪 Example Usage

Adjust the sliders for sepal and petal dimensions.

Click on the "Classify" button.

View the predicted Iris species along with the confidence probabilities.

📚 Acknowledgements

Dataset: The Iris dataset is sourced from the UCI Machine Learning Repository.

Tutorial Inspiration: Beginner’s Guide to Building an Iris Classification App with Streamlit

📄 License

This project is licensed under the MIT License - see the LICENSE
 file for details..
