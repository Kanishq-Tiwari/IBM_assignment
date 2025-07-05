AI Story Generator using GPT2-Medium
=====================================

This is a simple web app that generates short stories using Hugging Face's gpt2-medium model.

How to Run (Google Colab):
--------------------------
1. Install dependencies:
   !pip install -q streamlit pyngrok transformers torch

2. Save the following files:
   - story_generator.py
   - app.py
   - launch.py

3. Set your ngrok token inside launch.py:
   conf.get_default().auth_token = "your-ngrok-token"

4. Run launch.py in Colab to start the app.
   It will give you a public link using ngrok.

Requirements:
-------------
- transformers
- torch
- streamlit
- pyngrok
- ngrok account with token: https://dashboard.ngrok.com/get-started/your-authtoken

Model Used:
-----------
- gpt2-medium (downloaded from Hugging Face)

Author:
-------
Created by Kanishq Tiwari
