from collections import Counter
import math


print("===== Phishing Email Detection with ML =====")
print("Naive Bayes Classifier")
print("Training / Awareness Use Only\n")


# Small labeled training dataset
training_data = [
    ("urgent verify your account password immediately", "phishing"),
    ("click the link to verify your bank account", "phishing"),
    ("you won a prize provide your otp now", "phishing"),
    ("your account will be closed click here", "phishing"),
    ("confirm your password immediately", "phishing"),
    
    ("meeting scheduled for tomorrow at 10 am", "safe"),
    ("please find the project report attached", "safe"),
    ("team meeting has been moved to monday", "safe"),
    ("your assignment submission is due friday", "safe"),
    ("thank you for your email we will respond soon", "safe")
]


def tokenize(text):
    return text.lower().split()


class NaiveBayes:
    def __init__(self):
        self.class_counts = Counter()
        self.word_counts = {}
        self.total_words = {}
        self.vocabulary = set()

    def train(self, data):
        for text, label in data:
            words = tokenize(text)

            self.class_counts[label] += 1

            if label not in self.word_counts:
                self.word_counts[label] = Counter()
                self.total_words[label] = 0

            for word in words:
                self.word_counts[label][word] += 1
                self.total_words[label] += 1
                self.vocabulary.add(word)

    def predict(self, text):
        words = tokenize(text)
        total_documents = sum(self.class_counts.values())

        scores = {}

        for label in self.class_counts:
            # Calculate prior probability
            probability = self.class_counts[label] / total_documents

            # Calculate word probabilities
            for word in words:
                word_count = self.word_counts[label][word]
                vocabulary_size = len(self.vocabulary)

                # Laplace smoothing
                word_probability = (
                    (word_count + 1)
                    / (self.total_words[label] + vocabulary_size)
                )

                probability *= word_probability

            scores[label] = probability

        return max(scores, key=scores.get)


# Train the model
model = NaiveBayes()
model.train(training_data)

print("Model trained successfully.")
print("Training Emails:", len(training_data))


# Test emails
test_emails = [
    "URGENT click here to verify your password immediately",
    "The project meeting is scheduled for tomorrow"
]


print("\n===== Detection Results =====")

for email in test_emails:
    result = model.predict(email)

    print("\nEmail:", email)
    print("Prediction:", result.upper())


# Simple evaluation
correct = 0

for text, actual_label in training_data:
    prediction = model.predict(text)

    if prediction == actual_label:
        correct += 1


accuracy = (correct / len(training_data)) * 100

print("\n===== Model Evaluation =====")
print("Correct Predictions:", correct)
print("Total Samples:", len(training_data))
print("Accuracy:", f"{accuracy:.2f}%")

print("\nNote: This is a small educational dataset.")
print("It should not be used as a real-world phishing detection system.")

print("\nML Detection completed.")