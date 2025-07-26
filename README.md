Lapcraft F1

    Lapcraft F1 je open-source analytická platforma pro vizualizaci a porovnávání dat z formule 1 s využitím knihovny FastF1.

🚦 Hlavní funkce

    Interaktivní graf časů na kolo

        Barevné rozlišení podle směsi pneumatik

        Zobrazení detailních informací po najetí myší (čas, směs)

        Výběr libovolného závodu, jezdce a další

    Porovnání telemetrie dvou jezdců

        Přehledné grafy: rychlost, plyn, brzda, otáčky, rychlostní stupeň, DRS

        Synchronizované srovnání po celé délce okruhu

        Volba konkrétního kola pro každého jezdce zvlášť

    Pořadí týmů (konstruktérské body)

        Přehled aktuálních bodů týmů F1 v tabulce a grafu

        Barevné rozlišení týmů, automatická aktualizace dle nejnovějších dat

🏁 Jak aplikaci spustit

    (Doporučeno) Vytvoř virtuální prostředí:

python -m venv .venv

Aktivuj podle svého systému.

Nainstaluj potřebné knihovny:

pip install -r requirements.txt

Spusť aplikaci:

    streamlit run app.py

    V prohlížeči otevři http://localhost:8501

📦 Použité knihovny

    FastF1

    Streamlit

    Plotly

    numpy, scipy, pandas

Kompletní seznam najdete v souboru requirements.txt.
📝 Licence

Kód můžete volně používat, upravovat a šířit.
👨‍💻 Autor a právní informace

Projekt vytvořil: Jaroslav Chládek
Rok: 2025

    Lapcraft F1 je neoficiální komunitní nástroj určený pro analytické a vzdělávací účely v oblasti motorsportu.
    Aplikace ani její autor nejsou nijak spojeni s organizací Formula 1, FIA, FOM nebo s žádným závodním týmem.
    Veškerá použitá data jsou veřejně dostupná prostřednictvím platformy FastF1 a slouží pouze k nekomerčnímu využití.