import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom Styling with CSS
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        h1 {
            color: #222;
            font-size: 28px;
            font-weight: bold;
        }
        .bmi-category {
            font-size: 22px;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            margin-top: 10px;
        }
        .progress-bar {
            height: 12px;
            border-radius: 6px;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered Container
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title
st.markdown("<h1>⚖️ BMI Calculator</h1>", unsafe_allow_html=True)

# Input Fields with Columns
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter Weight (kg) 🔽", min_value=1.0, step=0.1, format="%.1f")
with col2:
    height_cm = st.number_input("Enter Height (cm) 📏", min_value=50.0, step=0.1, format="%.1f")

# Calculate BMI in real-time
if weight > 0 and height_cm > 0:
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight 😞"
        color = "#3498db"  # Blue
    elif 18.5 <= bmi < 24.9:
        category = "Normal ✅"
        color = "#2ecc71"  # Green
    elif 25 <= bmi < 29.9:
        category = "Overweight ⚠️"
        color = "#f39c12"  # Orange
    else:
        category = "Obese 🚨"
        color = "#e74c3c"  # Red

    # Display Results
    st.markdown(f'<h2 style="color:{color};">Your BMI: {bmi:.2f}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="bmi-category" style="background-color:{color}; color:white;">{category}</div>', unsafe_allow_html=True)

    # Animated Progress Bar
    st.progress(min(int((bmi / 40) * 100), 100))

else:
    st.warning("⚠️ Please enter valid weight and height.")

# Close Container
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🚀 Developed with Muhammad Sami ❤️ or  using Streamlit")
