import streamlit as st

st.title('AI AUDIOBOOK MAKING WOOHOOOOO')

st.header('Welcome to the AI Audiobook Making App!')

st.write('This app is created by oatmeal and plum for the AI Hackathon 2025.')

st.write('This app will help you convert your book text into an audiobook!')

st.write('To get started, please upload your book text file in the sidebar. Requirements: It must be a .txt file')

st.write('Once you have uploaded your file, you can select the voice you would like to use for the audiobook.')

st.write('After selecting the voice, you can click the "Create Audiobook" button to generate your audiobook!')

# txt. file only
uploaded_file = st.sidebar.file_uploader('Upload your book text file', type=['txt'])

# select a proper voice.
voice = st.sidebar.selectbox('Select the voice for your audiobook', ['Voice 1', 'Voice 2', 'Voice 3'])

if st.sidebar.button('Create Audiobook'):
    if uploaded_file is not None:
        st.write('Creating your audiobook...')
        # code to create the audiobook
    else:
        st.write('Please upload your book text file first!')
        