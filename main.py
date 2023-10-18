from __init__ import DSBApi  # Annahme, dass die Code-Datei DSBApi.py heißt

# Erstelle eine Instanz der DSBApi-Klasse mit deinem Benutzernamen und Passwort
api = DSBApi(username='23822', password='hagberlin')

# Rufe die DSBMobile-Einträge ab
entries = api.fetch_entries(images=True)  # Du kannst images auf False setzen, wenn du keine Bilder möchtest

# Verarbeite die Ergebnisse, z.B. gib sie aus
for entry in entries:
    print(entry)
