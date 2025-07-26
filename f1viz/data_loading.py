import fastf1
import datetime

def get_schedule(year):
    """Vrátí event schedule pro zadaný rok."""
    return fastf1.get_event_schedule(year)

def get_gp_names(schedule):
    """Vrátí seznam jmen závodů (bez testů)."""
    return [gp for gp in schedule['EventName'].tolist() if "Test" not in gp and "Testing" not in gp]

def get_session(year, gp_name, session_short, schedule):
    """
    Vrátí FastF1 session objekt a případnou chybovou hlášku.
    Pokud se závod ještě nejel, nebo není termín, vrací None a hlášku.
    """
    try:
        datum_zavodu = schedule[schedule['EventName'] == gp_name]['Session5Date'].values[0]
    except IndexError:
        return None, "Závod nebyl nalezen v kalendáři."

    if str(datum_zavodu) == 'NaT':
        return None, "Pro tento závod není známý termín nebo závod není v kalendáři."

    datum_zavodu = datetime.datetime.fromisoformat(str(datum_zavodu)).replace(tzinfo=None)
    ted = datetime.datetime.now()
    if datum_zavodu > ted:
        return None, "Tento závod se ještě nejel. Vyberte prosím jiný závod."

    session = fastf1.get_session(year, gp_name, session_short)
    session.load()
    return session, None
