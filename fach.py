class Fach:
    # Konstruktor-Methode für die Fach-Klasse, um Fachobjekte zu erstellen
    def __init__(self, name):
        self.name = name                        # Name des Fachs
        self.noten = []                         # Eine Liste zur Speicherung von Noten und deren Art
        self.schuelernummer = None              # Die Schülernummer, der das Fach zugeordnet ist

    # Methode zum Festlegen der Schülernummer, der dieses Fach gehört
    def set_schuelernummer(self, schuelernummer):
        self.schuelernummer = schuelernummer

    # Methode zum Hinzufügen einer Note zu diesem Fach
    def add_note_to_fach(self, art, note):
        if 1 <= note <= 6:
            self.noten.append((art, note))
        else:
            print(
                f"Ungültige Note ({note}) in Fach {self.name} für Schüler {self.schuelernummer}. Die Note darf nicht mehr als 6 betragen.")

    # Methode zum Bearbeiten oder Löschen einer Note basierend auf dem Index
    def edit_or_delete_note(self, index, new_note=None):
        if 0 <= index < len(self.noten):
            if new_note is not None:
                art, note = self.noten[index]
                self.noten[index] = (art, new_note)
            else:
                del self.noten[index]
        else:
            print("Ungültiger Index für die Note.")

    # Methode zur Berechnung der Durchschnittsnote für dieses Fach
    def berechne_durchschnittsnote(self):
        if not self.noten:
            return "Keine Noten verfügbar"  # Rückgabe einer Meldung, wenn keine Noten vorliegen

        summe_schulaufgaben = 0
        anzahl_schulaufgaben = 0
        summe_andere = 0

        for art, note in self.noten:
            if art == 'S':
                summe_schulaufgaben += note
                anzahl_schulaufgaben += 1
            else:
                summe_andere += note

        gesamt_durchschnitt = (summe_schulaufgaben + summe_andere) / len(self.noten)
        return round(gesamt_durchschnitt, 2)  # Runden Sie die Durchschnittsnote auf zwei Dezimalstellen

    # Methode zum Anzeigen der Noten und ihrer Art
    def display_grades(self):
        for i, (art, note) in enumerate(self.noten, start=1):
            print(f'{i}. Art: {art}, Note: {note}')
