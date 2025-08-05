import streamlit as st
import pandas as pd
import plotly.graph_objects as go

TEAM_COLORS = {
    "McLaren": "#FF8700",
    "Scuderia Ferrari": "#FF2800",
    "Mercedes-AMG Petronas Motorsport": "#27F4D2",
    "Red Bull Racing": "#1E41FF",
    "Williams": "#64C4FF",
    "Sauber": "#52E252",
    "Racing Bulls": "#6692FF",
    "Aston Martin F1 Team": "#229971",
    "Haas F1 Team": "#B6BABD",
    "Alpine F1 Team": "#2293D1",
}

data = {
    "Tým": [
        "McLaren",
        "Scuderia Ferrari",
        "Mercedes-AMG Petronas Motorsport",
        "Red Bull Racing",
        "Williams",
        "Sauber",
        "Racing Bulls",
        "Aston Martin F1 Team",
        "Haas F1 Team",
        "Alpine F1 Team"
    ],
    "Body": [559, 260, 236, 194, 70, 51, 45, 44, 35, 20]
}

def show_team_standings():
    #Sjednocený podnadpis
    st.markdown("""
        <style>
            .f1-subtitle {
                text-align: left;
                color: #fff;
                font-size: 2.1em;
                font-weight: 800;
                margin-bottom: 0.20em;
                margin-top: 0.05em;
                letter-spacing: 0.1px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        </style>
        <div class='f1-subtitle'>Pohár konstruktérů 2025</div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame(data)
    colors = [TEAM_COLORS.get(team, "#888888") for team in df["Tým"]]

    # Tabulka přes celou šířku
    st.dataframe(df, hide_index=True, use_container_width=True)

    # Sloupcový graf přes celou šířku
    fig = go.Figure(
        data=[go.Bar(
            x=df["Tým"],
            y=df["Body"],
            marker_color=colors
        )]
    )
    fig.update_layout(
        xaxis_title="Tým",
        yaxis_title="Body",
        plot_bgcolor="#191c24",
        paper_bgcolor="#191c24",
        font=dict(color="#fff", family="Segoe UI"),
        margin=dict(t=30, b=30, l=30, r=10)
    )
    st.plotly_chart(fig, use_container_width=True)




