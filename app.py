import streamlit as st
from f1viz.graf_kola import show_graf_kola
from f1viz.telemetrie import show_telemetrie
from f1viz.t_performance import show_team_standings
from f1viz.kalendar_f1 import show_calendar
from f1viz.compare_drivers import show_points_share

# --- Nastavení stránky, favicon a rozložení ---
st.set_page_config(
    page_title="Lapcraft F1",
    page_icon="🏎️",
)

# --- Globální styl (sjednocení vzhledu) ---
st.markdown("""
    <style>
        html, body, .main {background-color: #191c21 !important;}
        .f1-title {
            text-align: center;
            margin-bottom: 0.2em;
            color: #e30613;
            font-size: 2.25em;
            font-weight: 900;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
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

# --- Jednotný nadpis (refresh při kliknutí) ---
st.markdown(
    "<div class='f1-title'><a href='/' style='color: #e30613; text-decoration: none;'>Lapcraft F1</a></div>",
    unsafe_allow_html=True
)

# --- Hlavní navigace ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Graf časů",
    "Telemetrie",
    "Pořadí týmů",
    "Příští závod",
    "Body kolegů"
])

with tab1:
    show_graf_kola()
with tab2:
    show_telemetrie()
with tab3:
    show_team_standings()
with tab4:
    show_calendar()
with tab5:
    show_points_share()

# --- Copyright ---
st.markdown(
    "<p style='text-align: center; color: #888888; font-size: 15px; margin-top: 36px;'>"
    "© 2025 Jaroslav Chládek | Lapcraft F1"
    "</p>",
    unsafe_allow_html=True
)




