from pyngrok import conf, ngrok
import time

conf.get_default().auth_token = "your-auth-token" #read README.txt

!pkill -f streamlit
!pkill -f ngrok

get_ipython().system_raw('streamlit run app.py &')
time.sleep(5)

public_url = ngrok.connect(8501)
print(f"🔗 Your app is live at: {public_url}")

