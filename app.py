import os
import streamlit as st
from langchain.llms import OpenAI
from gtts import gTTS
from io import BytesIO
from googletrans import Translator

headers = {
    'Authorization': st.secrets["OPENAI_API_KEY"],
    "content-type": "application/json"
}

translation = Translator()

os.environ['OPENAI_API_KEY'] = apikey
#TITLE AND CONTENT
st.title("🐥TrienGPT")
prompt = st.text_input("INPUT DAAL DE BHAI")

#GETTING OUTPUT
llm = OpenAI(temperature = 0.9)
response = llm(prompt)



out_lang = st.selectbox(
    "Select your output language",
    ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Hindi":
    output_language = "hi"
elif out_lang == "Bengali":
    output_language = "bn"
elif out_lang == "korean":
    output_language = "ko"
elif out_lang == "Chinese":
    output_language = "zh-cn"
elif out_lang == "Japanese":
    output_language = "ja"


english_accent = st.selectbox(
    "Select your english accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "com"
elif english_accent == "India":
    tld = "co.in"

elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"

def Translation(response):
    translatedText = translation.translate(text = response, dest=output_language)
    return translatedText.text

def Text_to_speech(Output_language, response, tld):
    sound_file = BytesIO()
    tts = gTTS(response, lang=Output_language, tld = tld , slow = False)
    tts.write_to_fp(sound_file)
    return sound_file


display_output_text = st.checkbox("DISPLAY OUTPUT TEXT")


result_trans = Translation(response)
st.write(result_trans)

audio_file = Text_to_speech(output_language, result_trans, tld)
st.audio(audio_file)




