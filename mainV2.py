import dsbapi

ownFields = ['Klasse ','Stunde','Lehrer','Fach','Vertreter','Fach','Raum','empty','text']


dsbclient = dsbapi.DSBApi("238222", "hagberlin", tablemapper=ownFields)
entries = dsbclient.fetch_entries() # Rückgabe einer JSON Liste an Arrays

laenge = len(entries)

tablemapper = dsbclient.tablemapper

fehlende_Lehrer = []

for i in range(len(entries)):
    print("-------------------------------------------------------------------------------------------------")
    for k in range(len(entries[i])):
        print(entries[i][k])

for i in range(laenge):
    for k in range(len(entries[i])):
        fehlender_Lehrer = entries[i][k].get('Lehrer')
        if not fehlende_Lehrer.__contains__(fehlender_Lehrer):
            fehlende_Lehrer.append(fehlender_Lehrer)

print(fehlende_Lehrer)
