import streamlit as st
from PIL import Image

# Title of the app
st.title("Body Measurements Input (Inches)")

# Load the silhouette image
image = Image.open("pic02.jpg")  # Replace with the path to your silhouette image
st.image(image, use_column_width=True)

st.header("Enter Your Measurements (in inches)")

# Create input fields with labels positioned appropriately
col1, col2 = st.columns(2)

# Input fields for body measurements in inches
with col1:
    height_cm = st.number_input("Height (inches):", min_value=20, max_value=100, value=67)
    waist_inch = st.number_input("Waist Circumference (inches):", min_value=20, max_value=60, value=34)
    hip_inch = st.number_input("Hip Circumference (inches):", min_value=20, max_value=60, value=38)

with col2:
    weight_kg = st.number_input("Weight (lbs):", min_value=30, max_value=400, value=150)
    bust_inch = st.number_input("Chest Circumference (inches):", min_value=20, max_value=60, value=36)
  

# Body Shape Classifier Function
def classify_body_shape(bust, waist, hips):
    if abs(bust - hips) <= 2 and (waist < bust and waist < hips):
        return "Hourglass", "Fitted dresses, belted outfits, wrap tops"
    elif hips > bust and waist < hips:
        return "Pear (Triangle)", "A-line skirts, structured tops, wide-neck blouses"
    elif bust > hips and waist < bust:
        return "Inverted Triangle", "Flared skirts, V-neck tops, wide-leg pants"
    elif waist >= bust and waist >= hips:
        return "Apple (Round)", "Empire waist dresses, V-neck tops, flowy fabrics"
    else:
        return "Rectangle (Athletic/Straight)", "Peplum tops, layered outfits, ruched dresses"

# Additional inputs for body shape classification
st.header("Find Your Body Shape")


# Calculate BMI and Body Shape after submission
if st.button("Submit Measurements"):
    # Convert measurements to metric units for BMI calculation
   
    # Calculate BMI
    bmi = weight_kg / ((height_cm / 100) ** 2)

    # Display results
    st.success("Thank you for submitting your measurements!")
    st.write(f"Height: {height_cm} cm ")
    st.write(f"Weight: {weight_kg} kgs ")
    st.write(f"Waist Circumference: {waist_inch} inches")
    st.write(f"Hip Circumference: {hip_inch} inches")
    st.write(f"Chest Circumference: {bust_inch} inches")
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

    # Classify body shape
    if bust_inch and waist_inch and hips_inch:
        shape, tips = classify_body_shape(bust_inch, waist_inch, hips_inch)
        st.success(f"**Your Body Shape: {shape}**")
        st.info(f"**Recommended Clothing Styles:** {tips}")
    else:
        st.error("Please enter valid measurements.")

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
