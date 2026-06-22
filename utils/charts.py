import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def show_ats_gauge(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#ffe699"},
                    {"range": [70, 100], "color": "#d9ead3"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    st.plotly_chart(fig, use_container_width=True)


def show_skill_pie(matched_count, missing_count):

    df = pd.DataFrame({
        "Category": ["Matched Skills", "Missing Skills"],
        "Count": [matched_count, missing_count]
    })

    fig = px.pie(
        df,
        values="Count",
        names="Category",
        title="Skill Coverage"
    )

    st.plotly_chart(fig, use_container_width=True)