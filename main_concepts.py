# This is just the tutorial listed below + some notes + some small changes.
# src: tutorial at https://docs.streamlit.io/library/get-started/main-concepts 
import streamlit as st
import pandas as pd
import numpy as np

########################################################################
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# any time that Streamlit sees a variable or a literal value on its own line,
# it automatically writes that to your app using st.write()
df

st.write("Here's our *second* attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


dataframe = np.random.randn(10, 20)  # 10 rows, 20 cols filled w/ random nums
# make a table, with scrollbars
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),  # 10 rows, 20 cols filled w/ random nums
    columns=('col %d' % i for i in range(20))
)
# use Pandas Styler object to highlight some elements in the interactive table
st.dataframe(dataframe.style.highlight_max(axis=0))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
# make a static table, no scrollbars
st.table(dataframe)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# display lat, lon points on a map
# This sample data is of San Fran
st.map(map_data)



x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


# Or widgets can also be accessed by key, if you choose to specify 
# a string to use as the unique key for the widget
st.text_input("Your name", key="name")
# Every widget with a key is automatically added to a Session State.

# You can access the value at any point with:
st.write("Text input widget contains:", st.session_state.name)

if st.checkbox('Show secret message'):
    st.write("Have a fantastic day!")


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
