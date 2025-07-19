import streamlit as st

st.title("سلام دوست من! 👋")  
name = st.text_input("اسم تو چیه؟")  
if st.button("بزن بریم!"):  
    st.balloons()  # اینجا بادکنکها پرواز میکنند!  
    st.write(f"سلام {name}! خوش اومدی! 🎈")  