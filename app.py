import streamlit as st
import numpy as np
from PIL import Image  

# Title of the app  
st.title("Body Measurements Input (Inches)")  

# Load the silhouette image  
image = Image.open("Silhouette.png")  # Ensure this image exists in your working directory  

# Default image width (base value)
base_width = 200  

# Create a container for input fields  
with st.expander("Enter Your Measurements (in inches)", expanded=True):  
    col1, col2 = st.columns(2)  

    # Input fields for body measurements in inches  
    with col1:  
        height_inch = st.number_input("Height (inches):", min_value=20, max_value=100, value=65)  
        waist_inch = st.number_input("Waist Circumference (inches):", min_value=20, max_value=60, value=33)  
        hip_inch = st.number_input("Hip Circumference (inches):", min_value=20, max_value=60, value=34)  

    with col2:  
        weight_kg = st.number_input("Weight (kg):", min_value=30, max_value=400, value=70)  
        chest_inch = st.number_input("Chest Circumference (inches):", min_value=20, max_value=60, value=34)  
        neck_inch = st.number_input("Neck Circumference (inches):", min_value=10, max_value=30, value=15)  

# Convert height to cm
height_cm = height_inch * 2.54  

# Calculate BMI  
bmi = weight_kg / ((height_cm / 100) ** 2)  

# Adjust image width based on BMI or height  
scaled_width = int(base_width * (bmi / 22))  # Adjust width dynamically  
scaled_width = max(100, min(scaled_width, 400))  # Keep within reasonable limits  

# Display the dynamically resized silhouette image  
st.image(image, width=scaled_width)  

# Calculate BMI after submission  
if st.button("Submit Measurements"):  
    # Display results  
    st.success("Thank you for submitting your measurements!")  
    st.write(f"Height: {height_inch} inches ({height_cm:.2f} cm)")  
    st.write(f"Weight: {weight_kg} kg")  
    st.write(f"Waist Circumference: {waist_inch} inches")  
    st.write(f"Hip Circumference: {hip_inch} inches")  
    st.write(f"Chest Circumference: {chest_inch} inches")  
    st.write(f"Neck Circumference: {neck_inch} inches")  
    st.write(f"Calculated BMI: {bmi:.2f}")  

    # Provide useful tips based on BMI  
    if bmi < 18.5:  
        st.warning("Your BMI suggests that you are underweight. Consider consulting a healthcare provider.")  
    elif 18.5 <= bmi < 24.9:  
        st.success("Your BMI is in the normal range. Keep maintaining a healthy lifestyle!")  
    elif 24.9 <= bmi < 29.9:  
        st.warning("Your BMI suggests that you are overweight. Consider a balanced diet and regular exercise.")  
    else:  
        st.error("Your BMI indicates obesity. It's advisable to seek guidance from a healthcare provider.")  

# Provide additional resources with links  
st.header("Helpful Resources")  
st.markdown("""  
- [CDC BMI Calculator](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html)  
- [National Heart, Lung, and Blood Institute](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm)  
- [Healthy Eating Guidelines](https://www.choosemyplate.gov/)  
""")  

# Provide an option to restart the input process  
if st.button("Restart Measurements"):  
    st.experimental_rerun()  
