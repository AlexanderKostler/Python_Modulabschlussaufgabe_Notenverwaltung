class Schueler:
    # Konstruktor-Methode für die Schueler-Klasse, um Schülerobjekte zu erstellen
    def __init__(self, schuelernummer, vorname, nachname):
        self.schuelernummer = schuelernummer  # Eindeutige Schülernummer
        self.vorname = vorname                # Vorname des Schülers
        self.nachname = nachname              # Nachname des Schülers
        self.faecher = {}                     # Ein leeres Dictionary, um die Fächer des Schülers zu speichern
        self.durchschnittsnote = {}           # Ein leeres Dictionary für Durchschnittsnoten pro Fach

    # Methode zum Aktualisieren der Durchschnittsnoten für jedes Fach des Schülers
    def update_durchschnittsnote(self):
        for fachname, fach in self.faecher.items():
            durchschnittsnote_fach = fach.berechne_durchschnittsnote()
            self.durchschnittsnote[fachname] = durchschnittsnote_fach

    # Methode zum Anzeigen der Noten und Informationen über den Schüler
    def display_student_grades(self):
        print(f'\nSchüler: {self.vorname} {self.nachname} (Schülernummer: {self.schuelernummer})')
        for fachname, fach in self.faecher.items():
            durchschnittsnote_fach = fach.berechne_durchschnittsnote()
            if durchschnittsnote_fach is not None:
                print(f'\nFach: {fachname}, Durchschnittsnote: {durchschnittsnote_fach:.2f}')
            else:
                print(f'\nFach: {fachname}, Durchschnittsnote: Keine Noten verfügbar')
            print('Noten:')
            fach.display_grades()
