import streamlit as st
from googletrans import Translator, LANGUAGES


# Set page title and configuration
st.set_page_config(page_title="Language Converter")

# Apply custom CSS using st.markdown()
st.markdown(
    """
    <style>
    /* Add custom CSS here */
    .title {
        font-size: 2em;
        color: red;
        text-align: center;
        padding: 20px;
        background-color: yellow;
        border-radius: 10px;
        box-shadow: 2px 2px 5px 0px rgba(0,0,0,0.1);
    }

    .text {
        font-size: 1.2em;
        color: #333333;
    }

    .stButton>button {
        background-color: #1f77b4;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render styled elements
st.markdown('<h1 class="title">Language Converter</h1>', unsafe_allow_html=True)
st.markdown('<p class="text">This is a Language Converter UI. You can change it to your preferred language !</p>', unsafe_allow_html=True)

# Initialize the translator
translator = Translator()
#audio
st.audio("ad.m4a", format="audio/mpeg", loop=False)
# Streamlit app title
#st.title("Language Converter")
# Text input for the text to be translated
text_to_translate = st.text_area("Hi, Please enter text here to translate")

# Dropdowns for selecting source and target languages
source_language = st.selectbox("Select  your source language", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('en'))
target_language = st.selectbox("Select the target language you want ", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('es'))

# Language codes
source_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_language)]
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Translate button
if st.button("Translate"):
    st.write("Translated Successfully !")
    if text_to_translate:
        # Translate the text
        translation = translator.translate(text_to_translate, src=source_language_code, dest=target_language_code)
        # Display the translated text
        st.write(f"**Your Translated text:**_____ {translation.text}")
    else:
        st.error("Please enter some text to translate.")

# Add some additional instructions or information
st.write("Enter text in the text area above, select source and target languages, and click 'Translate' to see the translation.")


