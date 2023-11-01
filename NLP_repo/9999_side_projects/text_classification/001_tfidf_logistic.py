import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

import  os 
list1 = os.listdir()

print(list1)
print("=====================================")

# 1. Load the CSV data
data = pd.read_csv('courses_data_small.csv')

# 2. Preprocess the text data (optional: depending on the cleanliness of your data)
# For simplicity, I'm just converting all text to lowercase. You might want to do more.
data['course'] = data['course'].str.lower()

# 3. Convert the text data into a TF-IDF representation
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf = tfidf_vectorizer.fit_transform(data['course'])

# 4. Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(tfidf, data['title'], test_size=0.2, random_state=42)

# 5. Train a Logistic Regression model
clf = LogisticRegression(max_iter=1000)  # increased max_iter for convergence
clf.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("=-====================================")

# Function to predict the category of a new course description
def predict_category(course_description):
    # Transform the course description using our trained tf-idf vectorizer
    course_vec = tfidf_vectorizer.transform([course_description])
    # Use our trained classifier to make a prediction
    prediction = clf.predict(course_vec)
    return prediction[0]

# Predicting the category of a new course description
new_course_description = "Learn to play famous rock songs on your guitar"  # Replace with your description
predicted_category = predict_category(new_course_description)
print(f"The predicted category for the course is: {predicted_category}")

