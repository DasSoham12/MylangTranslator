import streamlit as st
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

API_key = 'AJQeVx4pXrwBb8B5QmIEgnmdsaEq6fXUKzavAzCinUul'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/eafb417c-aa96-4665-8ea3-021877acc94c'

## authenticating the API key
authenticator = IAMAuthenticator(apikey = API_key)

## setting our language object
langtranslator = LanguageTranslatorV3(version = '2018-05-01',
                                     authenticator = authenticator)

## establishing the connection with the service 
langtranslator.set_service_url(url)

st.title("Language-Translator")

# setting up the dropdown list of language 
option = st.selectbox(
    'Which Language would you choose to type',
    ('Arabic','Bengali','Bulgarian','Chinese (Simplified)','Chinese (Traditional)','Croatian','Dutch','English','French','German','Greek','Hindi','Gujarati','Irish','Italian','Japanese','Korean','Malayalam','Marathi','Nepali','Polish','Punjabi (Indian)','Russian','Slovenian','Spanish','Swedish','Tamil','Telegu','Thai','Turkish','Ukrainian','	Urdu'))

option2 = st.selectbox(
    'Which language would you like to translate to',
    ('Arabic','Bengali','Bulgarian','Chinese (Simplified)','Chinese (Traditional)','Croatian','Dutch','English','French','German','Greek','Hindi','Gujarati','Irish','Italian','Japanese','Korean','Malayalam','Marathi','Nepali','Polish','Punjabi (Indian)','Russian','Slovenian','Spanish','Swedish','Tamil','Telegu','Thai','Turkish','Ukrainian','	Urdu'))

sent = "Enter the text in "+option+" language in the text area below"

# setting up the dictionary of language to their keywords

language_library = {'Arabic':'ar','Bengali':'bn','Bulgarian':'bg','Chines(Simplified)':'zh','Croatian':'hr','Dutch':'nl','English':'en','French':'fr','German':'de','Greek':'el','Hindi':'hi','Gujarati':'gu','Irish':'ga','Italian':'it','Japanese':'ja','Korean':'ko','Malayalam':'ml','Marathi':'mr','Nepali':'ne','Polish':'pl','Punjabi(Indian)':'pa','Russian':'ru','Slovenian':'sl','Spanish':'es','Swedish':'sv','Tamil':'ta','Telegu':'te','Thai':'th','Turkish':'tr','Ukrainian':'uk','Urdu':'ur'}

sentence = st.text_area(sent, height=300)

#creating button named translate
if st.button("Translate"):  
    try:
        if option == option2:
            st.write("Please select different language for translation")
        else:
            #create the model_id for english to bengali en-bn, english to arabic en-ar....
            translate_code = language_library[option]+'-'+language_library[option2]
            
            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)
            
            ans = translation.get_result()['translations'][0]['translation']
            
            sent1 = 'Translated text in '+option2+' language is shown below'
            
            st.markdown(sent1)
            st.write(ans)
            
    except:
        st.write("Please do cross check if text-area is filled with sentence or not")
        