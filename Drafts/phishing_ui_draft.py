import streamlit as st
import joblib

# Load the trained phishing detection model
model = joblib.load("phishing_model.pkl")

# Streamlit UI
st.title("Phishing Detection Assistant")
st.write("Enter a message below to analyze whether it's phishing or legitimate.")

# Text input from user
user_input = st.text_area("Message to Analyze", height=150)

# Analyze button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        # Predict and get confidence
        prediction = model.predict([user_input])[0]
        confidence = model.predict_proba([user_input])[0]

        # Display result
        if prediction == 1:
            st.error("⚠️ This message is likely a PHISHING attempt.")
        else:
            st.success("✅ This message appears to be LEGITIMATE.")

        # Show confidence scores
        st.write("### Prediction Confidence")
        st.write(f"Legitimate: {confidence[0]*100:.2f}%")
        st.write(f"Phishing: {confidence[1]*100:.2f}%")
