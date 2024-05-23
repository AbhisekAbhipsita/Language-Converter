import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title("CSV File Uploader and Viewer")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.subheader("Dataframe")
    st.write(df)

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Select columns to plot
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns to plot", columns)

    if selected_columns:
        # Plot selected columns
        st.subheader("Data Visualization")
        fig, ax = plt.subplots()
        df[selected_columns].plot(ax=ax)
        st.pyplot(fig)

    st.write("File uploaded successfully!")
else:
    st.write("Please upload a CSV file to proceed.")

# Add some additional text or instructions
st.write("Upload a CSV file to see its content and basic statistics. You can also visualize selected columns.")
