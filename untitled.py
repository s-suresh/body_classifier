import streamlit as st
import pandas as pd
import pickle
import numpy as np

from PIL import Image  

# Title of the app  
st.title("Body Measurements Input (Inches)")  

# Load the silhouette image  
image = Image.open("silhouette.png")  # Replace with the path to your silhouette image  
st.image(image, use_column_width=True)  

st.header("Enter Your Measurements (in inches)")  

# Create input fields with labels positioned appropriately  
col1, col2 = st.columns(2)  

# Input fields for body measurements in inches  
with col1:  
    height_inch = st.number_input("Height (inches):", min_value=20, max_value=100, value=67)  
    waist_inch = st.number_input("Waist Circumference (inches):", min_value=20, max_value=60, value=34)  
    hip_inch = st.number_input("Hip Circumference (inches):", min_value=20, max_value=60, value=38)  

with col2:  
    weight_lb = st.number_input("Weight (kg):", min_value=30, max_value=400, value=150)  
    chest_inch = st.number_input("Chest Circumference (inches):", min_value=20, max_value=60, value=36)  
    neck_inch = st.number_input("Neck Circumference (inches):", min_value=10, max_value=30, value=15)  

# Calculate BMI after submission  
if st.button("Submit Measurements"):  
    # Convert measurements to metric units for BMI calculation  
    height_cm = height_inch * 2.54  # Convert inches to centimeters  
    weight_kg = weight_lb * 0.453592  # Convert pounds to kilograms  
    
    # Calculate BMI  
    bmi = weight_kg / ((height_cm / 100) ** 2)  
    
    # Display results  
    st.success("Thank you for submitting your measurements!")  
    st.write(f"Height: {height_inch} inches ({height_cm:.2f} cm)")  
    st.write(f"Weight: {weight_lb} lbs ({weight_kg:.2f} kg)")  
    st.write(f"Waist Circumference: {waist_inch} inches")  
    st.write(f"Hip Circumference: {hip_inch} inches")  
    st.write(f"Chest Circumference: {chest_inch} inches")  
    st.write(f"Neck Circumference: {neck_inch} inches")  
    st.write(f"Calculated BMI: {bmi:.2f}")  

    # Provide useful tips based on BMI  
    if bmi < 18.5:  
        st.write("Tip: Your BMI suggests that you are underweight. Consider consulting a healthcare provider.")  
    elif 18.5 <= bmi < 24.9:  
        st.write("Tip: Your BMI is in the normal range. Keep maintaining a healthy lifestyle!")  
    elif 25 <= bmi < 29.9:  
        st.write("Tip: Your BMI suggests that you are overweight. Consider a balanced diet and regular exercise.")  
    else:  
        st.write("Tip: Your BMI indicates obesity. It's advisable to seek guidance from a healthcare provider.")  

# Provide additional resources with links  
st.header("Helpful Resources")  
st.markdown("""  
- [CDC BMI Calculator](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html): Use this to check your BMI against standard weight categories.  
- [National Heart, Lung, and Blood Institute](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm): Find more information about BMI and its relevance to health.  
- [Healthy Eating Guidelines](https://www.choosemyplate.gov/): Explore tips for maintaining a balanced diet.  
""")  
# Provide an option to restart the input process  
if st.button("Restart Measurements"):  
    st.experimental_rerun()
