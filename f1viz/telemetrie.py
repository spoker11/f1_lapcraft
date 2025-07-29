import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import interp1d
import time

from f1viz.data_loading import get_schedule, get_gp_names, get_session
from f1viz.utils import TEAM_COLORS

def show_telemetrie():
    # --- Sjednocený podnadpis ---
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
        </style>
        <div class='f1-subtitle'>Porovnání telemetrie</div>
    """, unsafe_allow_html=True)

    with st.form("telemetrie_form"):
        year = st.selectbox("Sezóna", list(range(2020, 2026))[::-1], index=1)
        schedule = get_schedule(year)
        gp_names = get_gp_names(schedule)

        gp_name = st.selectbox("Velká cena", gp_names)
        session_type = st.selectbox("Část víkendu", ["FP1", "FP2", "FP3", "Qualifying", "Race"])
        session_short = session_type

        session, err = get_session(year, gp_name, session_short, schedule)
        drivers = session.laps['Driver'].unique().tolist() if session and not err else []

        col1, col2 = st.columns(2)
        with col1:
            driver1 = st.selectbox("První jezdec", drivers if drivers else ["N/A"], index=0)
        with col2:
            driver2 = st.selectbox(
                "Druhý jezdec",
                [d for d in drivers if d != (drivers[0] if drivers else "")] if drivers else ["N/A"],
                index=0 if drivers and len(drivers) > 1 else 0
            )

        laps1 = session.laps.pick_driver(driver1) if session and drivers and driver1 != "N/A" else None
        laps2 = session.laps.pick_driver(driver2) if session and drivers and driver2 != "N/A" else None

        lap_nums1 = laps1["LapNumber"].astype(int).tolist() if laps1 is not None else []
        lap_nums2 = laps2["LapNumber"].astype(int).tolist() if laps2 is not None else []

        col1, col2 = st.columns(2)
        with col1:
            lap1 = st.selectbox(
                f"Kolo pro {driver1}",
                lap_nums1 if lap_nums1 else [1],
                key=f"lap1_{driver1}"  # KLÍČ závislý na jménu jezdce
            )
        with col2:
            lap2 = st.selectbox(
                f"Kolo pro {driver2}",
                lap_nums2 if lap_nums2 else [1],
                key=f"lap2_{driver2}"  # KLÍČ závislý na jménu jezdce
            )

        submitted = st.form_submit_button("Zobrazit")

    if not submitted:
        st.info("Vyber všechna pole.")
        return

    if err:
        st.warning(err)
        return

    if laps1 is None or laps2 is None or driver1 == "N/A" or driver2 == "N/A":
        st.warning("Nejsou dostupná data pro vybrané jezdce.")
        return

    with st.spinner("Načítám data a připravuji graf…"):
        lap1_row = laps1[laps1["LapNumber"] == lap1].iloc[0]
        lap2_row = laps2[laps2["LapNumber"] == lap2].iloc[0]

        car_data1 = lap1_row.get_car_data().add_distance()
        car_data2 = lap2_row.get_car_data().add_distance()

        tcolor1 = TEAM_COLORS.get(lap1_row['Team'], '#888888')
        tcolor2 = TEAM_COLORS.get(lap2_row['Team'], '#888888')
        lname1 = session.get_driver(driver1)['LastName']
        lname2 = session.get_driver(driver2)['LastName']

        dist_common = np.linspace(
            max(car_data1['Distance'].min(), car_data2['Distance'].min()),
            min(car_data1['Distance'].max(), car_data2['Distance'].max()),
            num=1000
        )

        speed1 = interp1d(car_data1['Distance'], car_data1['Speed'], fill_value="extrapolate")(dist_common)
        speed2 = interp1d(car_data2['Distance'], car_data2['Speed'], fill_value="extrapolate")(dist_common)
        throttle1 = interp1d(car_data1['Distance'], car_data1['Throttle'], fill_value="extrapolate")(dist_common)
        throttle2 = interp1d(car_data2['Distance'], car_data2['Throttle'], fill_value="extrapolate")(dist_common)
        brake1 = interp1d(car_data1['Distance'], car_data1['Brake'], fill_value="extrapolate")(dist_common)
        brake2 = interp1d(car_data2['Distance'], car_data2['Brake'], fill_value="extrapolate")(dist_common)
        rpm1 = interp1d(car_data1['Distance'], car_data1['RPM'], fill_value="extrapolate")(dist_common)
        rpm2 = interp1d(car_data2['Distance'], car_data2['RPM'], fill_value="extrapolate")(dist_common)
        gear1 = interp1d(car_data1['Distance'], car_data1['nGear'], fill_value="extrapolate")(dist_common)
        gear2 = interp1d(car_data2['Distance'], car_data2['nGear'], fill_value="extrapolate")(dist_common)
        drs1 = interp1d(car_data1['Distance'], car_data1['DRS'], fill_value="extrapolate")(dist_common)
        drs2 = interp1d(car_data2['Distance'], car_data2['DRS'], fill_value="extrapolate")(dist_common)

        rows = 6
        fig = make_subplots(
            rows=rows, cols=1, shared_xaxes=True,
            vertical_spacing=0.03,
        )
        # RYCHLOST
        fig.add_trace(go.Scatter(
            x=dist_common, y=speed1, line=dict(color=tcolor1),
            name=lname1,
            legendgroup="1",
            hovertemplate="%{y:.0f} km/h"
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=speed2, line=dict(color=tcolor2),
            name=lname2,
            legendgroup="2",
            hovertemplate="%{y:.0f} km/h"
        ), row=1, col=1)
        # PLYN
        fig.add_trace(go.Scatter(
            x=dist_common, y=throttle1, line=dict(color=tcolor1, dash="dot"),
            showlegend=False,
            name="",
            hovertemplate="%{y:.0f} %"
        ), row=2, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=throttle2, line=dict(color=tcolor2, dash="dot"),
            showlegend=False,
            name="",
            hovertemplate="%{y:.0f} %"
        ), row=2, col=1)
        # BRZDA
        fig.add_trace(go.Scatter(
            x=dist_common, y=brake1, line=dict(color=tcolor1),
            showlegend=False,
            name="",
            hovertemplate="%{customdata}",
            customdata=[("ON" if v > 0.5 else "OFF") for v in brake1]
        ), row=3, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=brake2, line=dict(color=tcolor2),
            showlegend=False,
            name="",
            hovertemplate="%{customdata}",
            customdata=[("ON" if v > 0.5 else "OFF") for v in brake2]
        ), row=3, col=1)
        # RPM
        fig.add_trace(go.Scatter(
            x=dist_common, y=rpm1, line=dict(color=tcolor1),
            showlegend=False,
            name="",
            hovertemplate="%{y:.0f} RPM"
        ), row=4, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=rpm2, line=dict(color=tcolor2),
            showlegend=False,
            name="",
            hovertemplate="%{y:.0f} RPM"
        ), row=4, col=1)
        # RYCHLOSTNÍ STUPEŇ
        fig.add_trace(go.Scatter(
            x=dist_common, y=gear1, line=dict(color=tcolor1),
            showlegend=False,
            name="",
            hovertemplate="Stupeň: %{y:.0f}"
        ), row=5, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=gear2, line=dict(color=tcolor2),
            showlegend=False,
            name="",
            hovertemplate="Stupeň: %{y:.0f}"
        ), row=5, col=1)
        # DRS
        fig.add_trace(go.Scatter(
            x=dist_common, y=drs1, line=dict(color=tcolor1),
            showlegend=False,
            name="",
            hovertemplate="%{customdata}",
            customdata=[("ON" if v > 0.5 else "OFF") for v in drs1]
        ), row=6, col=1)
        fig.add_trace(go.Scatter(
            x=dist_common, y=drs2, line=dict(color=tcolor2),
            showlegend=False,
            name="",
            hovertemplate="%{customdata}",
            customdata=[("ON" if v > 0.5 else "OFF") for v in drs2]
        ), row=6, col=1)

        fig.update_layout(
            template="plotly_dark",
            height=1050,
            plot_bgcolor="#191c24",
            paper_bgcolor="#191c24",
            font=dict(family="Segoe UI,Arial", size=14),
            legend=dict(orientation="h", y=1.08, x=0.5, xanchor="center"),
            margin=dict(l=30, r=10, t=10, b=20)
        )
        fig['layout']['yaxis1']['title'] = "Rychlost (km/h)"
        fig['layout']['yaxis2']['title'] = "Plyn (%)"
        fig['layout']['yaxis3']['title'] = "Brzda"
        fig['layout']['yaxis4']['title'] = "RPM"
        fig['layout']['yaxis5']['title'] = "Rychlostní stupeň"
        fig['layout']['yaxis6']['title'] = "DRS"
        fig['layout']['xaxis6']['title'] = "Vzdálenost na kolo (m)"

        time.sleep(1)
        st.plotly_chart(fig, use_container_width=True)


