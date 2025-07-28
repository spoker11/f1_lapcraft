import streamlit as st

def show_points_share():
    teams = [
        {
            "team": "Aston Martin",
            "driver1": "Fernando Alonso",
            "driver2": "Lance Stroll",
            "points1": 41,
            "points2": 0,
            "color": "#229971"
        },
        {
            "team": "Sauber",
            "driver1": "Valtteri Bottas",
            "driver2": "Zhou Guanyu",
            "points1": 12,
            "points2": 0,
            "color": "#39FF14"
        },
        {
            "team": "Alpine",
            "driver1": "Pierre Gasly",
            "driver2": "Esteban Ocon",
            "points1": 5,
            "points2": 0,
            "color": "#FFB6C1"
        },
        {
            "team": "Racing Bulls",
            "driver1": "Daniel Ricciardo",
            "driver2": "Yuki Tsunoda",
            "points1": 21,
            "points2": 0,
            "color": "#2853e8"
        },
        {
            "team": "Red Bull",
            "driver1": "Max Verstappen",
            "driver2": "Sergio Pérez",
            "points1": 255,
            "points2": 18,
            "color": "#1E41FF"
        },
        {
            "team": "Williams",
            "driver1": "Alex Albon",
            "driver2": "Logan Sargeant",
            "points1": 18,
            "points2": 5,
            "color": "#00BFFF"
        },
        {
            "team": "Haas",
            "driver1": "Nico Hülkenberg",
            "driver2": "Kevin Magnussen",
            "points1": 7,
            "points2": 3,
            "color": "#B6BABD"
        },
        {
            "team": "Mercedes",
            "driver1": "Lewis Hamilton",
            "driver2": "George Russell",
            "points1": 56,
            "points2": 28,
            "color": "#27F4D2"
        },
        {
            "team": "Ferrari",
            "driver1": "Charles Leclerc",
            "driver2": "Carlos Sainz",
            "points1": 120,
            "points2": 102,
            "color": "#FF2800"
        },
        {
            "team": "McLaren",
            "driver1": "Oscar Piastri",
            "driver2": "Lando Norris",
            "points1": 105,
            "points2": 98,
            "color": "#FF8700"
        }
    ]

    st.title("Podíl bodů mezi týmovými kolegy F1 2025")

    for t in teams:
        total = t["points1"] + t["points2"]
        pct1 = 100 * t["points1"] / total if total else 0
        pct2 = 100 * t["points2"] / total if total else 0

        col1, col2, col3 = st.columns([2, 6, 2])
        with col1:
            st.markdown(f"<div style='font-weight:700; color:white;'>{t['driver1']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:1.7em; color:{t['color']}; font-weight:700'>{pct1:.0f}%</div>", unsafe_allow_html=True)
        with col2:
            bar_html = f"""
                <div style='background:#333; border-radius:6px; width:100%; height:32px; position:relative; margin:8px 0;'>
                    <div style='background:{t['color']}; height:100%; width:{pct1:.0f}%; border-radius:6px 0 0 6px; display:inline-block;'></div>
                    <div style='background:#666; height:100%; width:{pct2:.0f}%; border-radius:0 6px 6px 0; display:inline-block;'></div>
                </div>
            """
            st.markdown(bar_html, unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center; font-size:1.2em; color:#ccc; font-weight:500;'>{t['team']}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div style='font-size:1.7em; color:#888; font-weight:700'>{pct2:.0f}%</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-weight:700; color:white;'>{t['driver2']}</div>", unsafe_allow_html=True)

        st.markdown(f"<div style='height:16px;'></div>", unsafe_allow_html=True)

