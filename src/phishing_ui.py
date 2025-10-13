"""
Copyright 2025 Dwayne Winn

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---
How to run this Streamlit app:

1. Open a terminal or PowerShell window.
2. Run the following command (quotes are important due to spaces in the path):

   streamlit run "C:\Users\D L Winn\source\repos\dlwinn44\Cognitive-Cybersecurity-Assistant-CCA-\src\phishing_ui.py"

3. The app will launch in your default web browser.

This is a working prototype. Ready for the next module prototype.
"""

import streamlit as st
import joblib

# Load the trained phishing detection model
model = joblib.load("C:\\Users\\D L Winn\\source\\repos\\dlwinn44\\Cognitive-Cybersecurity-Assistant-CCA-\\src\\phishing_model.pkl")

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
