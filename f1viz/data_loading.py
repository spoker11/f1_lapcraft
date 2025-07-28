import fastf1
import datetime


def get_schedule(year):
    """Vrátí event schedule pro zadaný rok."""
    return fastf1.get_event_schedule(year)


def get_gp_names(schedule):
    """Vrátí seznam jmen závodů (bez testů)."""
    return [gp for gp in schedule['EventName'].tolist() if "Test" not in gp and "Testing" not in gp]


def get_location_slug(schedule, gp_name):
    """Vrátí slug (Location) pro vybraný závod."""
    filtered = schedule[schedule['EventName'] == gp_name]
    if filtered.empty:
        return None
    return filtered['Location'].values[0].lower()  # např. 'bahrain', 'imola'


def get_session(year, gp_name, session_short, schedule):
    """
    Vrátí FastF1 session objekt a případnou chybovou hlášku.
    Pokud se závod ještě nejel, nebo není termín, vrací None a hlášku.
    """
    filtered = schedule[schedule['EventName'] == gp_name]
    if filtered.empty:
        return None, "Závod nebyl nalezen v kalendáři."

    datum_zavodu = filtered['Session5Date'].values[0]
    if str(datum_zavodu) == 'NaT':
        return None, "Pro tento závod není známý termín nebo závod není v kalendáři."

    datum_zavodu = datetime.datetime.fromisoformat(str(datum_zavodu)).replace(tzinfo=None)
    ted = datetime.datetime.now()
    if datum_zavodu > ted:
        return None, "Tento závod se ještě nejel. Vyberte prosím jiný závod."

    slug = get_location_slug(schedule, gp_name)
    if not slug:
        return None, "Slug pro tento závod nebyl nalezen (zkontroluj data schedule)."

    try:
        session = fastf1.get_session(year, slug, session_short)
        session.load()
    except Exception as e:
        return None, f"Chyba při načítání session: {str(e)}"
    return session, None

