# Barvy týmů (2024, F1TV styl)
TEAM_COLORS = {
    "Red Bull Racing": "#1E41FF",
    "Ferrari": "#FF2800",
    "Mercedes": "#27F4D2",
    "McLaren": "#FF8700",
    "Aston Martin": "#229971",
    "Alpine": "#2293D1",
    "Williams": "#64C4FF",
    "RB": "#6692FF",          # Visa Cash App RB
    "Haas F1 Team": "#B6BABD",
    "Kick Sauber": "#52E252",
    "Alfa Romeo": "#C92D4B",  # Pro starší ročníky
    "AlphaTauri": "#2B4562",  # Pro starší ročníky
}

# Barvy směsí pneumatik
color_dict = {
    "SOFT": "#ff3655",      # červená
    "MEDIUM": "#ffe900",    # žlutá
    "HARD": "#ffffff",      # bílá
    "INTERMEDIATE": "#27b14a", # zelená
    "WET": "#0090ff",       # modrá
    "UNKNOWN": "#888888",
    None: "#888888"
}

# Emojis ke směsím (volitelné, pro tooltipy)
emoji_dict = {
    "SOFT": "🔴",
    "MEDIUM": "🟡",
    "HARD": "⚪",
    "INTERMEDIATE": "🟢",
    "WET": "🔵",
    "UNKNOWN": "⚫",
    None: "⚫"
}

# Formátování času na kolo
def format_laptime_simple(seconds, ms=True):
    """
    Vrací čas ve formátu M:SS nebo M:SS.sss podle parametru ms.
    """
    if seconds is None or seconds != seconds:
        return "-"
    try:
        seconds = float(seconds)
    except Exception:
        return str(seconds)
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if ms:
        return f"{minutes}:{sec:02}.{millis:03}"
    else:
        return f"{minutes}:{sec:02}"

