import pickle

# Load trained objects
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("intent_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_intent(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]