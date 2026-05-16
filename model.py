import pickle

# Load trained objects
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("intent_model.pkl", "rb") as f:
    model = pickle.load(f)

MIN_CONFIDENCE = 0.12

def predict_intent(text):
    vec = vectorizer.transform([text])
    probabilities = model.predict_proba(vec)[0]
    best_index = probabilities.argmax()

    if probabilities[best_index] < MIN_CONFIDENCE:
        return "unknown"

    return model.classes_[best_index]
