import dsbapi
from flask import Flask, render_template

ownFields = ['Klasse', 'Stunde', 'Lehrer', 'Fach', 'Vertreter', 'Fach', 'Raum', 'empty', 'text']

app = Flask(__name__)


@app.route('/')
def index():
    dsbclient = dsbapi.DSBApi("238222", "hagberlin", tablemapper=ownFields)
    entries = dsbclient.fetch_entries()

    def getFehlendeLehrer():

        fehlende_Lehrer = {}

        for entry in entries:
            lehrer = entry.get('Lehrer')
            tag = entry.get('date')
            if lehrer and tag:
                if tag in fehlende_Lehrer:
                    fehlende_Lehrer[tag].append(lehrer)
                else:
                    fehlende_Lehrer[tag] = [lehrer]

        return fehlende_Lehrer

    meineLehrer = ['Schindler', 'Opolka', 'Schenker', 'Dahncke', 'Brach', 'Gnielka', 'Rogge']

    nichtDa = getFehlendeLehrer()

    ausfälle = {}

    for tag, lehrer_set in nichtDa.items():
        for lehrer in meineLehrer:
            if lehrer in lehrer_set:
                if tag in ausfälle:
                    ausfälle[tag].append(lehrer)
                else:
                    ausfälle[tag] = [lehrer]

    return render_template('index.html', ausfälle=ausfälle)


if __name__ == '__main__':
    app.run(debug=True)
