import streamlit as st
import datetime

def show_calendar():
    # --- Nastavení informací o dalším závodě ---
    next_race_name = "Velká cena Nizozemska"
    next_race_title = "Začíná za:"
    next_race_date = "2025-08-31"
    next_race_time = "15:00"   # 24h format

    # Sestavení datetime pro závod
    race_dt = datetime.datetime.strptime(f"{next_race_date} {next_race_time}", "%Y-%m-%d %H:%M")
    now = datetime.datetime.now()
    time_left = race_dt - now

    # Odpočet
    days = time_left.days if time_left.days >= 0 else 0
    hours = time_left.seconds // 3600 if time_left.days >= 0 else 0
    minutes = (time_left.seconds // 60) % 60 if time_left.days >= 0 else 0

    st.markdown("""
    <style>
    .f1-subtitle {
        text-align: center;
        color: #fff;
        font-size: 2.1em;
        font-weight: 800;
        margin-bottom: 0.20em;
        margin-top: 0.05em;
        letter-spacing: 0.1px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    .nextup-title { text-align:center; color:#fff; font-size:1.5em; font-weight:700; margin-bottom:0.08em;}
    .nextup-timer { display:flex; justify-content:center; gap:25px; margin-bottom:0.8em; margin-top:1.5em;}
    .nextup-box { background:#18191c; border-radius:18px; padding:12px 26px; color:#fff; font-family:monospace;
                  font-size:2.25em; font-weight:700; text-align:center; min-width:80px; }
    .nextup-box-label { font-size:0.43em; font-weight:500; color:#fff; letter-spacing:1px;}
    </style>
    """, unsafe_allow_html=True)

    # --- Nadpis stejného stylu jako ostatní podstránky ---
    st.markdown(f"<div class='f1-subtitle'>{next_race_name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='nextup-title'>{next_race_title}</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='nextup-timer'>"
        f"<div class='nextup-box'>{days:02d}<div class='nextup-box-label'>days</div></div>"
        f"<div class='nextup-box'>{hours:02d}<div class='nextup-box-label'>hours</div></div>"
        f"<div class='nextup-box'>{minutes:02d}<div class='nextup-box-label'>min</div></div>"
        "</div>",
        unsafe_allow_html=True
    )









