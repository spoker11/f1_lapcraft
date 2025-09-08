import streamlit as st

def show_points_share():
    teams = [
        {
            "team": "Aston Martin",
            "driver1": "Fernando Alonso",
            "driver2": "Lance Stroll",
            "points1": 30,
            "points2": 32,
            "color": "#229971"
        },
        {
            "team": "Kick Sauber",
            "driver1": "Nico Hülkenberg",
            "driver2": "Gabriel Bortoleto",
            "points1": 37,
            "points2": 18,
            "color": "#39FF14"
        },
        {
            "team": "Alpine",
            "driver1": "Pierre Gasly",
            "driver2": "Franco Colapinto",
            "points1": 20,
            "points2": 0,
            "color": "#FFB6C1"
        },
        {
            "team": "Racing Bulls",
            "driver1": "Liam Lawson",
            "driver2": "Isack Hadjar",
            "points1": 20,
            "points2": 38,
            "color": "#2853e8"
        },
        {
            "team": "Red Bull",
            "driver1": "Max Verstappen",
            "driver2": "Júki Cunoda",
            "points1": 230,
            "points2": 12,
            "color": "#1E41FF"
        },
        {
            "team": "Williams",
            "driver1": "Alex Albon",
            "driver2": "Carlos Sainz",
            "points1": 70,
            "points2": 16,
            "color": "#00BFFF"
        },
        {
            "team": "Haas",
            "driver1": "Esteban Ocon",
            "driver2": "Oliver Bearman",
            "points1": 28,
            "points2": 16,
            "color": "#B6BABD"
        },
        {
            "team": "Mercedes",
            "driver1": "Kimi Antonelli",
            "driver2": "George Russell",
            "points1": 66,
            "points2": 194,
            "color": "#27F4D2"
        },
        {
            "team": "Ferrari",
            "driver1": "Charles Leclerc",
            "driver2": "Lewis Hamilton",
            "points1": 163,
            "points2": 117,
            "color": "#FF2800"
        },
        {
            "team": "McLaren",
            "driver1": "Oscar Piastri",
            "driver2": "Lando Norris",
            "points1": 324,
            "points2": 293,
            "color": "#FF8700"
        }
    ]

    # Jednotný nadpis a box pro porovnání
    st.markdown("<div class='f1-subtitle'>Podíl bodů mezi týmovými kolegy</div>", unsafe_allow_html=True)
    st.markdown("<div class='f1-card'>", unsafe_allow_html=True)

    # Přidaný klíč pct1 (procentualni podil jezdce) pro řazení
    for t in teams:
        total = t["points1"] + t["points2"]
        t["pct1"] = 100 * t["points1"] / total if total else 0

    # Seřazeno sestupně podle pct1
    teams = sorted(teams, key=lambda x: x["pct1"], reverse=True)

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
                <div style='background:transparent; border-radius:6px; width:100%; height:32px; position:relative; margin:8px 0;'>
                    <div style='background:{t['color']}; height:100%; width:{pct1:.0f}%; border-radius:6px 0 0 6px; display:inline-block;'></div>
                </div>
            """
            st.markdown(bar_html, unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center; font-size:1.2em; color:#ccc; font-weight:500; margin-bottom:10px'>{t['team']}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div style='font-weight:700; color:white;'>{t['driver2']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:1.7em; color:#888; font-weight:700'>{pct2:.0f}%</div>", unsafe_allow_html=True)

        st.markdown(f"<div style='height:16px;'></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
