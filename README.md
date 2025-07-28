🏎️ Lapcraft F1

Lapcraft F1 je open-source analytická platforma pro vizualizaci a porovnání dat z Formule 1 s využitím knihovny FastF1.
Projekt je určen pro fanoušky, studenty i analytiky, kteří chtějí nahlédnout pod pokličku F1 dat.
🚦 Hlavní funkce

    Graf časů na kolo

        Interaktivní zobrazení časů na kolo pro vybraného jezdce a závod

        Barevné rozlišení podle směsi pneumatik

        Podrobné info při najetí myší na bod (čas, směs)

        Výběr ročníku, závodu, jezdce a session

    Porovnání telemetrie dvou jezdců

        Srovnávací grafy: rychlost, plyn, brzda, otáčky, rychlostní stupeň, DRS

        Data konkrétního kola pro oba jezdce

        Synchronizované zobrazení po celé délce okruhu

    Přehled pořadí týmů (konstruktérské body)

        Tabulka a graf bodového zisku týmů v aktuální sezóně

        Automatická aktualizace podle nejnovějších dat

        Barevné rozlišení podle týmových barev

    Kalendář & odpočet na další závod

        Stránka s informacemi o příštím závodě

        Reálný countdown do startu

        Přehled detailů (okruh, čas startu, atd.)

    Podíl bodů mezi týmovými kolegy

        Graf rozložení bodů mezi jezdci v rámci týmu

        Barevná vizualizace a jednoduché porovnání

🏁 Jak aplikaci spustit

    Vytvoř virtuální prostředí (doporučeno):

python -m venv .venv

Aktivuj podle svého systému:

    Linux/Mac: source .venv/bin/activate

    Windows: .venv\Scripts\activate

Nainstaluj požadované knihovny:

pip install -r requirements.txt

Spusť aplikaci:

    streamlit run app.py

    A otevři http://localhost:8501 ve svém prohlížeči.

📦 Použité knihovny

    FastF1

    Streamlit

    Plotly

    numpy, scipy, pandas
    Kompletní seznam v souboru requirements.txt.

📝 Licence

Tento projekt je k dispozici pod otevřenou licencí (viz soubor LICENSE).
Kód můžete volně používat, upravovat i šířit.
👨‍💻 Autor & Právní informace

Autor: Jaroslav Chládek
Rok: 2025

    Lapcraft F1 je neoficiální komunitní nástroj pro analytické a vzdělávací účely v motorsportu.
    Aplikace ani autor nejsou nijak spojeni s organizací Formula 1, FIA, FOM, ani se žádným závodním týmem.
    Veškerá data pochází z veřejné platformy FastF1 a slouží pouze k nekomerčnímu použití.