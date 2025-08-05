import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
from f1viz.data_loading import get_schedule, get_gp_names, get_session
from f1viz.utils import TEAM_COLORS, color_dict, emoji_dict

def format_laptime_simple(seconds):
    if np.isnan(seconds):
        return "-"
    m = int(seconds // 60)
    s = seconds % 60
    return f"{m}:{s:06.3f}"

def show_graf_kola():
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
        <div class='f1-subtitle'>Graf časů na kolo</div>
    """, unsafe_allow_html=True)

    # Výběr základních parametrů (uložíme do session_state)
    with st.form("graf_kola_form"):
        years = list(range(2020, 2026))[::-1]
        year = st.selectbox("Sezóna", years, index=1, key="year")
        schedule = get_schedule(year)
        gp_names = get_gp_names(schedule)
        gp = st.selectbox("Velká cena", gp_names, key="gp")
        sessions = ["FP1", "FP2", "FP3", "Qualifying", "Race"]
        session_name = st.selectbox("Část víkendu", sessions, index=0, key="session_name")
        submit = st.form_submit_button("Načíst data")

    if submit:
        st.session_state["last_params"] = {
            "year": year,
            "gp": gp,
            "session_name": session_name,
        }

    # Pokud uživatel vybral a potvrdil parametry, tak se pokračuje
    params = st.session_state.get("last_params")
    if not params:
        st.info("Vyber všechny možnosti a klikni na 'Načíst data'.")
        return

    with st.spinner("Načítám session a jezdce…"):
        session, err = get_session(params["year"], params["gp"], params["session_name"], get_schedule(params["year"]))
        if err:
            st.warning(err)
            return
        drivers = session.laps['Driver'].unique().tolist() if session else []
        if not drivers:
            st.warning("Nebyli nalezeni žádní jezdci pro tuto session.")
            return

    # Samostatný výběr jezdce (mimo formulář = zůstává na stránce)
    driver = st.selectbox("Jezdec", drivers, key="driver_pick")
    if not driver:
        st.warning("Vyber jezdce.")
        return

    laps = session.laps.pick_driver(driver)
    if laps.empty:
        st.warning("Pro zvoleného jezdce nejsou k dispozici žádná platná kola.")
        return

    with st.spinner("Načítám data a připravuji graf…"):
        best_lap = laps['LapTime'].min()
        laps['is_outlier'] = laps['LapTime'] > (best_lap * 1.10)
        laps['is_valid'] = laps['LapTime'].notna()
        filtered_laps = laps.copy()
        filtered_laps = filtered_laps[~filtered_laps['is_outlier']]
        filtered_laps = filtered_laps[filtered_laps['is_valid']]

        if filtered_laps.empty:
            st.warning("Pro tento filtr nejsou žádná kola k dispozici.")
            return

        lap_numbers = filtered_laps['LapNumber'].astype(int).values
        lap_times = filtered_laps['LapTime'].dt.total_seconds().values
        compounds = filtered_laps['Compound'].values

        marker_colors = [color_dict.get(c, "#888") for c in compounds]
        hover_texts = [
            f"Kolo: {lap_numbers[i]}<br>Čas: {format_laptime_simple(lap_times[i])}<br>{compounds[i]} {emoji_dict.get(compounds[i], '')}"
            for i in range(len(lap_numbers))
        ]

        team_name = session.get_driver(driver)['TeamName']
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=lap_numbers,
            y=lap_times,
            mode="lines+markers",
            line=dict(color=TEAM_COLORS.get(team_name, "#888"), width=3),
            marker=dict(
                color=marker_colors,
                size=10,
                line=dict(width=1, color='#222')
            ),
            name=driver,
            hovertemplate='%{customdata}',
            customdata=hover_texts
        ))

        yticks = np.linspace(min(lap_times), max(lap_times), 8)
        yticklabels = [format_laptime_simple(v) for v in yticks]

        fig.update_layout(
            margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor="#191c21",
            paper_bgcolor="#191c21",
            font=dict(color="#FFF"),
            xaxis=dict(title="Číslo kola"),
            yaxis=dict(
                title="Čas na kolo",
                tickvals=yticks,
                ticktext=yticklabels
            ),
            hoverlabel=dict(font_size=15)
        )

        time.sleep(1)
        st.plotly_chart(fig, use_container_width=True)




