## MySideEffect


**Problem:**
There is a lot of medical research going on, but usually there is no real information about it other than on the prescription. Additionally, not all side effects are distributed equally, or you are even allergic to some ingredients.

**Solution:**
* Tapping publically available adverse side effects data and putting it in context of individual patient profile
* Potential in Future: Analyzing medical science papers about adverse side effects, save them and keep the information updated
* Provide a interface for searching the name of a drug, and showing old and new information about it
* Based on a Symptom, showing relevant drugs and the severity and frequency of their side effects
* If you create a user-profile, drugs irrelevant for you (based on allergies, location (availability), preferences, ...) will not be shown
* The more information there is about a patient, the more specific and helpful are the suggestions going to be


**Data resources:**
* OpenFDA Adverse event data - https://open.fda.gov/downloads/
* PubMed (MEDLINE) - API for bulk download: https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/
* * SIDER (side effect database, extracted from public documents and package inserts, last update: October 2015) - http://sideeffects.embl.de/
* MEDRA (Dictionary of medical terms): https://www.meddra.org/
* PUBCHEM (Database of drug compounds): https://pubchem.ncbi.nlm.nih.gov/ https://pubchem.ncbi.nlm.nih.gov/pug_rest/PUG_REST.html

This is part of the [BaselHack](baselhack.ch) Hackathon: https://github.com/BaselHack/BaselHack2017/wiki/Topics 
