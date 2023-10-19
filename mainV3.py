import dsbapi

ownFields = ['Klasse', 'Stunde', 'Lehrer', 'Fach', 'Vertreter', 'Fach', 'Raum', 'empty', 'text']

dsbclient = dsbapi.DSBApi("238222", "hagberlin", tablemapper=ownFields)
entries = dsbclient.fetch_entries()  

fehlende_Lehrer = {}

for entry in entries:
    for event in entry:
        lehrer = event.get('Lehrer')
        tag = event.get('date')
        if lehrer:
            if tag in fehlende_Lehrer:
                fehlende_Lehrer[tag].append(lehrer)
            else:
                fehlende_Lehrer[tag] = [lehrer]

for tag, lehrer_list in fehlende_Lehrer.items():
    print(f"Am {tag} fehlen folgende Lehrer: {', '.join(lehrer_list)}")
