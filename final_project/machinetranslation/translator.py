import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Task 1 - Create Instance of Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


# Task 2 - Create English French Function
def translater_english_to_french(english_text):
    french_text = ""
    if english_text is not None:
        translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        # french_text = json.dumps(translation, indent=2, ensure_ascii=False)
        french_text = translation["translations"][0]["translation"]
    return french_text


# Task 3 - Create French English Function
def translater_french_to_english(french_text):
    english_text = ""
    if french_text is not None:
        translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        # english_text = json.dumps(translation, indent=2, ensure_ascii=False)
        english_text = translation["translations"][0]["translation"]
    return english_text
