import streamlit as st
from f1viz.graf_kola import show_graf_kola
from f1viz.telemetrie import show_telemetrie
from f1viz.t_performance import show_team_standings
from f1viz.kalendar_f1 import show_calendar

# --- Favicon a nadpis záložky ---
st.set_page_config(
    page_title="F1 LapCraft",
    page_icon="🏎️",
)

# --- Styl pro zarovnání záložek a nadpisu ---
st.markdown("""
    <style>
    .centered {text-align: center; margin-bottom: 0.3em;}
    div[data-testid="stTabs"] > div {justify-content: center;}
    button[data-baseweb="tab"] {
        font-size: 1.10rem; padding: 0.25em 2em; margin-right: 0.8em;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #e30613 !important;
        color: white !important;
        border-radius: 7px 7px 0 0 !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Nadpis na střed s odkazem (refresh)
st.markdown("""
    <h1 class='centered'>
        <a href='/' style='color: #e30613; text-decoration: none;'>Lapcraft F1</a>
    </h1>
""", unsafe_allow_html=True)

# --- Tabs nativně, pod nadpisem ---
tab1, tab2, tab3, tab4 = st.tabs([
    "Graf časů na kolo",
    "Porovnání telemetrie",
    "Pořadí týmů",
    "Příští závod"
])

with tab1:
    show_graf_kola()
with tab2:
    show_telemetrie()
with tab3:
    show_team_standings()
with tab4:
    show_calendar()

# Copyright na střed
st.markdown(
    "<p style='text-align: center; color: #888888; font-size: 16px; margin-top: 36px;'>"
    "© 2025 Jaroslav Chládek"
    "</p>",
    unsafe_allow_html=True
)

