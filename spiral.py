from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
`/spiral.py` :heart: streamlit [documentation](https://docs.streamlit.io) and [community forums](https://discuss.streamlit.io)
"""

dot_color = '#0068c9'
color_num = 0

def change_color():
    global dot_color
    global color_num
    color_num = (color_num + 50) % 100
    dot_color = '#FF00' + f"{color_num:02}"

#change_color()

left_column, right_column = st.columns(2)
with left_column:
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
with right_column:
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

# draw the code on the app, then execute it
with st.echo(code_location='below'):

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    df = pd.DataFrame(data)

    st.altair_chart(alt.Chart(df, height=500, width=500)
        .mark_circle(color=dot_color, opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

    st.write(df)
    st.write(f"min x is {df['x'].min()}")
    st.write(f"max x is {df['x'].max()}")
    st.write(f"min y is {df['y'].min()}")
    st.write(f"max y is {df['y'].max()}")
