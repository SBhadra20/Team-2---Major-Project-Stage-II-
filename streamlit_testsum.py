# -*- coding: utf-8 -*-
"""Streamlit Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/130Y6Ly_5MIN9fV1oc27XcsRqp6bBWtjt
"""

!pip install lightning transformers

!pip install pytorch-lightning==1.2.2

from google.colab import drive
drive.mount('/content/drive')

import lightning as pl
from transformers import AdamW, T5ForConditionalGeneration, T5TokenizerFast as T5Tokenizer
import pickle
MODEL_NAME = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME,model_max_length=512)

model = pickle.load(open('/content/drive/MyDrive/t5.pkl', 'rb'))

# Commented out IPython magic to ensure Python compatibility.
# %%writefile get_output.py
# import lightning as pl
# from transformers import AdamW, T5ForConditionalGeneration, T5TokenizerFast as T5Tokenizer
# import pickle
# MODEL_NAME = "t5-base"
# tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME,model_max_length=512)
# 
# model = pickle.load(open('/content/drive/MyDrive/t5.pkl', 'rb'))
# 
# def encode_text(text):
#     # Encode the text using the tokenizer
#     encoding = tokenizer.encode_plus(
#         text,
#         max_length=512,
#         padding="max_length",
#         truncation=True,
#         return_attention_mask=True,
#         return_tensors='pt'
#     )
#     return encoding["input_ids"], encoding["attention_mask"]
# 
# def generate_summary(input_ids, attention_mask):
#     # Generate a summary using the best model
#     generated_ids = model.generate(
#         input_ids=input_ids,
#         attention_mask=attention_mask,
#         max_length=150,
#         num_beams=2,
#         repetition_penalty=2.5,
#         length_penalty=1.0,
#         early_stopping=True
#     )
#     return generated_ids
# 
# def decode_summary(generated_ids):
#     # Decode the generated summary
#     summary = [tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces=True)
#                for gen_id in generated_ids]
#     return "".join(summary)
# 
# def summarize(text):
#     input_ids, attention_mask = encode_text(text)
#     generated_ids = generate_summary(input_ids, attention_mask)
#     summary = decode_summary(generated_ids)
#     return summary

def encode_text(text):
    # Encode the text using the tokenizer
    encoding = tokenizer.encode_plus(
        text,
        max_length=512,
        padding="max_length",
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )
    return encoding["input_ids"], encoding["attention_mask"]

def generate_summary(input_ids, attention_mask):
    # Generate a summary using the best model
    generated_ids = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=150,
        num_beams=2,
        repetition_penalty=2.5,
        length_penalty=1.0,
        early_stopping=True
    )
    return generated_ids

def decode_summary(generated_ids):
    # Decode the generated summary
    summary = [tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces=True)
               for gen_id in generated_ids]
    return "".join(summary)

def summarize(text):
    input_ids, attention_mask = encode_text(text)
    generated_ids = generate_summary(input_ids, attention_mask)
    summary = decode_summary(generated_ids)
    return summary

text="""Mumbai: Captain Harmanpreet Kaur called it a “dream” after Mumbai Indians emerged champions of the inaugural Women’s Premier League here on Sunday.
MI first restricted Delhi Capitals to 131 for nine and then overhauled the target with three balls to spare to record a seven wicket win in the summit clash.
“It has been a great experience, we were waiting for this for so many years. Everyone enjoyed this throughout the dressing room. It feels like a dream, for everyone
here,” Harmanpreet said during the post-match presentation. “So many people were asking when WPL will come and that day is here, and we are so happy and proud.” 
MI were 23 for 2 in the fourth over while chasing 132 to win but Nat Sciver-Brunt smashed a 55-ball 60 not out to take them home. “I think having a long batting
line-up, we had to go there and express. Very happy with how everyone performed. I think staying positive is key, we were lucky with full tosses going in our favour,”
the MI skipper said. “This is a special moment for all of us, I have been waiting a long time and today I know what it feels like to be winning. We keep talking 
about being positive, and we executed our plans really well and that’s the reason I’m standing here today.”
"""

print(summarize(text))

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import time
# from get_output import summarize
# 
# # Set up Streamlit app
# st.set_page_config(page_title='Text Summarizer')
# st.title('Text Summarizer')
# st.subheader('Developed using T5 transformer and trained on news data.')
# 
# text_input = st.text_input(label='Enter text to summarize')
# 
# if st.button('Summarize'):
#     # Summarize input text
#     if text_input:
#       start = time.time()
#       output = summarize(text_input)
#       endtime = time.time()
#       st.text(f'Total Time taken for Summarizing {endtime-start} seconds')
#       col1, col2 = st.beta_columns(2)
#       with col1:
#           st.subheader('Original Text')
#           st.write(text_input)
#       with col2:
#           st.subheader('Summary')
#           st.write(output)

!npm install localtunnel

!streamlit run /content/app.py &>/content/logs.txt &

!npx localtunnel --port 8501

