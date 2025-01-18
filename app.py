import streamlit as st
import matplotlib.pyplot as plt

# App title
st.title("Scatter Plot Generator with Button")

# Input for x and y values
x_values = st.text_input("Enter x values (comma separated)", "1, 2, 3, 4, 5")
y_values = st.text_input("Enter y values (comma separated)", "2, 3, 4, 5, 6")

# Convert input strings to lists of numbers
x_list = list(map(float, x_values.split(',')))
y_list = list(map(float, y_values.split(',')))

# Create a button to display the plot
if st.button("Generate Plot"):
    # Ensure x and y lists have the same length
    if len(x_list) == len(y_list):
        # Create scatter plot
        fig, ax = plt.subplots()
        ax.scatter(x_list, y_list, color='blue', label='Data Points')
        ax.set_title("Scatter Plot")
        ax.set_xlabel("X Values")
        ax.set_ylabel("Y Values")
        ax.legend()

        # Display plot in the Streamlit app
        st.pyplot(fig)
    else:
        st.error("The number of x values must be equal to the number of y values.")
