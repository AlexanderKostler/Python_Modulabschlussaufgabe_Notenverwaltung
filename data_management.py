import os  # Importiert das Modul "os" zur Arbeit mit Dateipfaden/-namen
from schueler import Schueler  # Importiert die Klasse "Schueler" aus dem Modul "schueler"
from fach import Fach  # Importiert die Klasse "Fach" aus dem Modul "fach"


# Diese Funktion importiert Schülerdaten aus einer Textdatei und erstellt ein Schüler-Datenbank-Dictionary
def importiere_schuelerdatei(dateiname):
    schueler_dict = {}
    klassenname = os.path.basename(dateiname).split('.')[0]
    # Überprüft, ob der Klassenname ungültig ist (z. B. leere Zeichenkette)
    if not klassenname:
        print("\nUngültiger Dateiname. Bitte wiederholen.")
        return schueler_dict  # Gibt ein leeres Dictionary zurück

    try:
        with open(dateiname, 'r') as datei:  # Öffnet die Datei im Lesemodus
            for zeile_num, zeile in enumerate(datei, start=1):  # Schleife durch jede Zeile der Datei
                daten = zeile.strip().split()  # Trennt die Zeile in Daten
                # Überprüft, ob die Anzahl der Daten in einer Zeile nicht gleich 6 ist
                if len(daten) != 6:
                    print(f"Fehler in Zeile {zeile_num}: Ungültige Daten - {zeile}")
                    continue
                # Extrahiert Daten für Schülernummer, Vorname, Nachname, Fach, Art und Note
                schuelernummer, vorname, nachname, fach, art, note = daten
                # Überprüft, ob die Schülernummer mit 'S' beginnt (gültig)
                if not schuelernummer.startswith('S'):
                    print(f"Ungültige Schülernummer ({schuelernummer}). Die Schülernummer muss mit 'S' beginnen.")
                    continue
                # Wenn die Schülernummer noch nicht im Dictionary existiert, wird ein neuer Schüler erstellt
                if schuelernummer not in schueler_dict:
                    schueler_dict[schuelernummer] = Schueler(schuelernummer, vorname, nachname)
                    schueler = schueler_dict[schuelernummer]
                # Wenn das Fach im Schülerobjekt nicht existiert, wird ein neues Fach erstellt
                if fach not in schueler.faecher:
                    schueler.faecher[fach] = Fach(fach)  # Hier wird ein neues Fach-Objekt erstellt
                    schueler.faecher[fach].set_schuelernummer(schuelernummer)
                fach_obj = schueler.faecher[fach]  # Holt das Fach-Objekt für den Schüler
                fach_obj.add_note_to_fach(art, int(note))  # Fügt eine Note zum Fach hinzu

        for schuelernummer, schueler in schueler_dict.items():
            schueler.update_durchschnittsnote()
    except FileNotFoundError:
        print(f"\nUngültiger Dateiname ({dateiname}). Bitte wiederholen.")

    return schueler_dict


# Diese Funktion exportiert Schülerdaten in eine Textdatei oder ein anderes Dateiformat
def exportiere_schuelerdaten(schueler_dict, file_path):
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as datei:
            for schuelernummer, schueler in schueler_dict.items():
                datei.write(f'Schülernummer: {schuelernummer}\n')
                datei.write(f'Vorname: {schueler.vorname}\n')
                datei.write(f'Nachname: {schueler.nachname}\n')
                datei.write('Fächer und Durchschnittsnoten:\n')
                for fachname, durchschnittsnote in schueler.durchschnittsnote.items():
                    datei.write(f'- {fachname}: {durchschnittsnote:.2f}\n')
                datei.write('\n')
        print(f'\nSchülerdaten wurden in den selben Pfad wie das Programm unter dem Namen "{file_path}" exportiert.')


# Diese Funktion berechnet Statistikdaten für die Schüler und Fächer
def berechne_statistikdaten(schueler_dict):
    gesamtnoten = {}  # Ein Dictionary, um Gesamtnoten für jedes Fach zu speichern
    schueler_pro_fach = {}  # Ein Dictionary, um die Anzahl der Schüler pro Fach zu speichern

    for schuelernummer, schueler in schueler_dict.items():
        for fachname, fach in schueler.faecher.items():
            durchschnittsnote_fach = fach.berechne_durchschnittsnote()  # Holt die Durchschnittsnote für das Fach

            if fachname not in gesamtnoten:
                gesamtnoten[fachname] = 0
            gesamtnoten[fachname] += durchschnittsnote_fach  # Addiert die Durchschnittsnote zu den Gesamtnoten

            if fachname not in schueler_pro_fach:
                schueler_pro_fach[fachname] = 0
            schueler_pro_fach[fachname] += 1  # Erhöht die Anzahl der Schüler pro Fach um 1

    return gesamtnoten, schueler_pro_fach  # Gibt die Gesamtnoten und Schüler pro Fach zurück


def anzeigen_statistikdaten(gesamtnoten, schueler_pro_fach):
    print("Statistikdaten pro Fach:")
    for fachname in gesamtnoten:
        durchschnittsnote_fach = gesamtnoten[fachname] / schueler_pro_fach[fachname]
        print(f'- {fachname}: Durchschnittsnote {durchschnittsnote_fach:.2f}')

    gesamtdurchschnitt = sum(gesamtnoten.values()) / sum(schueler_pro_fach.values())
    print(f"Durchschnittsnote der Klasse: {gesamtdurchschnitt:.2f}")


def display_all_student_grades(schueler_dict):
    for schuelernummer, schueler in schueler_dict.items():
        schueler.display_student_grades()
