import streamlit as st
import pandas as pd
import numpy as np


st.title("This is the title")
st.markdown("This is the markdown")
st.header("This is the header")
st.subheader("This is the subheader")

"""
# header
a
## subsheadrr
"""

a = {
    "key": "val"
}
a
mylist = [1,2,4]
st.write(mylist)

st.sidebar.write("This is the sidebar")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

df

st.image("https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

option = st.selectbox(
    'Which dashboard?',
    ('twitter', 'wallstreetbets', 'stocktwits', 'chart', 'pattern'))
st.write('You selected:', option)