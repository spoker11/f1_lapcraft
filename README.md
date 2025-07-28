🏎️ Lapcraft F1

Lapcraft F1 je open-source analytická platforma pro vizualizaci a porovnávání dat z formule 1 s využitím knihovny FastF1.
Projekt je navržený pro fanoušky, studenty i analytiky, kteří chtějí objevovat zákulisí F1 dat.
🚦 Hlavní funkce
1. Graf časů na kolo

    Interaktivní zobrazení časů na kolo pro vybraného jezdce a závod

    Barevné rozlišení podle směsi pneumatik

    Podrobné informace (čas, směs) při najetí myší na bod

    Možnost výběru ročníku, závodu, jezdce a session

2. Porovnání telemetrie dvou jezdců

    Srovnávací grafy: rychlost, plyn, brzda, otáčky, rychlostní stupeň, DRS

    Data zvolené session a konkrétního kola pro oba jezdce

    Synchronizované zobrazení po celé délce okruhu

3. Přehled pořadí týmů (konstruktérské body)

    Tabulka a graf bodového zisku týmů v aktuální sezoně

    Automatická aktualizace podle nejnovějších dat

    Barevné rozlišení podle týmových barev

4. Kalendář a countdown na příští závod

    Stránka s informacemi o následujícím závodě

    Reálný odpočet do startu

    Přehled základních detailů (okruh, čas startu...)

5. Vizualizace bodového podílu týmových kolegů

    Porovnání rozložení bodů mezi jezdci v rámci týmu

    Barevná vizualizace a jednoduché porovnání

🏁 Jak aplikaci spustit
1. Vytvoř virtuální prostředí (doporučeno)

python -m venv .venv

Aktivuj podle svého systému (např. source .venv/bin/activate nebo .venv\Scripts\activate).
2. Nainstaluj požadované knihovny

pip install -r requirements.txt

3. Spusť aplikaci

streamlit run app.py

A otevři http://localhost:8501 ve svém prohlížeči.
📦 Použité knihovny

    FastF1

    Streamlit

    Plotly

    numpy, scipy, pandas
    Kompletní seznam najdete v souboru requirements.txt.

📝 Licence

Projekt je k dispozici pod otevřenou licencí. Kód můžete volně používat, upravovat i šířit.
👨‍💻 Autor a právní informace

Autor: Jaroslav Chládek
Rok: 2025

    Lapcraft F1 je neoficiální komunitní nástroj určený pro analytické a vzdělávací účely v oblasti motorsportu.
    Aplikace ani její autor nejsou nijak spojeni s organizací Formula 1, FIA, FOM nebo s žádným závodním týmem.
    Veškerá použitá data jsou veřejně dostupná prostřednictvím platformy FastF1 a slouží pouze k nekomerčnímu využití.