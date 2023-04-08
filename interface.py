import streamlit as st
import streamlit.components.v1 as components
import textsummarizer

components.html("""
<head>
    <title>Text Summarizer</title>
</head>
    <h1> Upload the text file </h1>
""")


file_input = st.file_uploader("Choose a file", type=['txt'])
summary_size = st.text_input("Enter number of sentences required in the summary: ", placeholder = "Example: 5", )
button = st.button("Summarize")

if file_input is not None:

    bytes_data = file_input.getvalue()
    string_data = bytes_data.decode("utf-8")

    if button:

        output_text = textsummarizer.summarizer(string_data, int(summary_size))

        st.write(output_text)
