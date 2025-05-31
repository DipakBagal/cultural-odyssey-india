# utils/visualization.py

import altair as alt

def line_chart(df, x_col, y_col, color_col):
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X(x_col, type='temporal'),
        y=alt.Y(y_col, type='quantitative'),
        color=alt.Color(color_col, type='nominal'),
        tooltip=[x_col, y_col, color_col]
    ).interactive()
    return chart

def bar_chart(df, x_col, y_col, color_col):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(x_col, type='nominal'),
        y=alt.Y(y_col, type='quantitative'),
        color=alt.Color(color_col, type='nominal'),
        tooltip=[x_col, y_col, color_col]
    ).interactive()
    return chart