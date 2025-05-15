# Streamlit

import streamlit as st
import pickle
import pandas as pd

# بارگذاری مدل
with open("model/best_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# بارگذاری داده‌ها
df = pd.read_csv("data/processed_data.csv")

# رابط کاربری Streamlit
st.title("تشخیص تراکنش‌های تقلبی")
st.write("یک تراکنش را وارد کنید تا آن را تحلیل کنیم.")

# ورودی‌ها برای ویژگی‌های مهم
amount = st.number_input("مقدار تراکنش", min_value=0.0)
device_type = st.selectbox("نوع دستگاه", df["Device_Type"].unique())

# دکمه پیش‌بینی
if st.button("تحلیل تراکنش"):
    input_data = pd.DataFrame([[amount, device_type]], columns=["Transaction_Amount", "Device_Type"])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🚨 این تراکنش مشکوک به تقلب است!")
    else:
        st.success("✅ این تراکنش معتبر به نظر می‌رسد.")

