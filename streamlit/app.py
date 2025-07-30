import streamlit as st
import numpy as np 
import pandas as pd

# title of app

st.title("Hello StreamLit")

# simple text
st.write('This is simple text')

# create df
df = pd.DataFrame({
    "1": [1, 2, 3, 4, 5],
    "2": [10, 20, 30, 40 , 50]
})

st.write('show data frame')
st.write(df)

# line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a', 'b', 'c']
)

st.line_chart(chart_data)



# inputs

st.title('Inputs')

name = st.text_input("Enter you name")

if name:
    st.write(f'your name is {name}')