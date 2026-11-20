
import streamlit as st

st.set_page_config(page_title="Smart Pricing Assistant")

st.title("Smart Pricing Assistant")
st.write("مساعد ذكي لحساب سعر البيع والهامش الربحي بسرعة.")

currency = st.selectbox("اختر العملة", ["د.ج", "EUR", "USD"])
cost = st.number_input("سعر التكلفة", min_value=0.0, value=100.0)
margin = st.slider("نسبة هامش الربح (%)", 0, 200, 39)

if st.button("احسب السعر المقترح"):
    selling_price = cost * (1 + margin / 100)
    profit = selling_price - cost
    st.success(f"سعر البيع المقترح: {selling_price:.2f} {currency}")
    st.info(f"قيمة الربح: {profit:.2f} {currency}")
