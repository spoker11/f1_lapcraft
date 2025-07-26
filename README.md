# Lapcraft F1

**Lapcraft F1** je open-source analytická platforma pro vizualizaci a porovnávání dat z formule 1 s využitím knihovny FastF1.  



## Hlavní funkce

- **Interaktivní graf časů na kolo**  
  - Barevné rozlišení podle směsi pneumatik
  - Zobrazení detailních informací po najetí myší (čas, směs)
  - Výběr libovolného závodu, jezdce a další

- **Porovnání telemetrie dvou jezdců**  
  - Přehledné grafy: rychlost, plyn, brzda, otáčky, rychlostní stupeň, DRS
  - Synchronizované srovnání po celé délce okruhu
  - Volba konkrétního kola pro každého jezdce zvlášť

---

## Jak aplikaci spustit

1. **(Doporučeno)** Použij virtuální prostředí  
   (např. vytvoříš příkazem `python -m venv .venv` a aktivuješ podle svého systému)

2. **Nainstaluj potřebné knihovny:**  
    ```bash
    pip install -r requirements.txt
    ```

3. **Spusť aplikaci:**  
    ```bash
    streamlit run app.py
    ```

4. V prohlížeči otevři [http://localhost:8501](http://localhost:8501)


---

## Použité knihovny

- [FastF1](https://theoehrly.github.io/Fast-F1/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- numpy, scipy, pandas

Kompletní seznam najdete v souboru [requirements.txt](requirements.txt).


---

## Licence

Kód můžete volně používat, upravovat a šířit.

---

## Autor a právní informace

Projekt vytvořil: **Jaroslav Chládek**  
Rok: 2025

Lapcraft F1 je neoficiální komunitní nástroj určený pro analytické a vzdělávací účely v oblasti motorsportu.  
Aplikace ani její autor nejsou nijak spojeni s organizací Formula 1, FIA, FOM nebo s žádným závodním týmem.  
Veškerá použitá data jsou veřejně dostupná prostřednictvím platformy FastF1 a slouží pouze k nekomerčnímu využití.
