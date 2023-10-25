# Importieren der benötigten Funktionen aus data_management
from data_management import importiere_schuelerdatei, exportiere_schuelerdaten, berechne_statistikdaten, anzeigen_statistikdaten


# Funktion zur Anzeige des Willkommensbanners
def display_welcome_banner():
    welcome_banner = '''
               _                                                                     _                                                                               
              | |                              _                                    | |                                                                         _    
 _ _ _   ____ | |  ____  ___   ____    ____   | |_   ___      ____   ____  ____   _ | |  ____    ____    ____  ____    ____   ____   ____  ____    ____  ____  | |_  
| | | | / _  )| | / ___)/ _ \ |    \  / _  )  |  _) / _ \    / _  | / ___)/ _  | / || | / _  )  |    \  / _  ||  _ \  / _  | / _  | / _  )|    \  / _  )|  _ \ |  _) 
| | | |( (/ / | |( (___| |_| || | | |( (/ /   | |__| |_| |  ( ( | || |   ( ( | |( (_| |( (/ /   | | | |( ( | || | | |( ( | |( ( | |( (/ / | | | |( (/ / | | | || |__ 
 \____| \____)|_| \____)\___/ |_|_|_| \____)   \___)\___/    \_|| ||_|    \_||_| \____| \____)  |_|_|_| \_||_||_| |_| \_||_| \_|| | \____)|_|_|_| \____)|_| |_| \___)
                                                            (_____|                                                         (_____|                                  
    '''
    print(welcome_banner)
    print("**********************************************************************"
          "\nBevor Sie das Programm starten, bitte ich Sie, die Anleitung zu lesen! "
          "\nDie allgemeinen Funktionen lauten:\n"
          "\n6. Schülerdaten exportieren \n7. Schülerdaten importieren \n8. Programm beenden.\n "
          "\nDie Funktionen mit Nummern 1-5 sind erst dann relevant, wenn die Funktion 7 erfolgreich ausgeführt wurde.\n"
          "\n!!!Daher bitte ich Sie die Nummer 7 zuerst zu verwenden!!!\n"
          "**********************************************************************")
    input("\nUm fortzufahren ... drücken Sie [ENTER]↵")

# Diese Funktion zeigt die Noten aller Schüler an, die im Schüler-Daten-Dictionary (schueler_dict) gespeichert sind.


def display_all_student_grades(schueler_dict):
    for schuelernummer, schueler in schueler_dict.items():
        schueler.display_student_grades()


def validate_note_type(input_text):
    allowed_values = ["S", "M", "A", "E"]
    if input_text not in allowed_values:
        raise ValueError("Ungültige Eingabe. Bitte geben Sie S, M, A oder E ein.")

# UI-Hauptmenü


def user_interface(schueler_dict):
    import_completed = False  # Wird auf True gesetzt, wenn die Option 7 (Schülerdaten importieren) abgeschlossen ist

    while True:
        print("\nNotenverwaltungsprogramm - Hauptmenü:")

        # Schleife, die so lange läuft, bis Option 7 abgeschlossen ist
        while not import_completed:
            print("\n7. Schülerdaten importieren")
            choice = input("\nWählen Sie eine Option (7): ")

            if choice == "7":
                import_dateiname = input("\nGeben Sie den Dateinamen für den Import ein: ")
                schueler_dict = importiere_schuelerdatei(import_dateiname)
                import_completed = True  # Option 7 abgeschlossen
            else:
                print("Bitte die 7 eingeben, um Schülerdaten zu importieren.")

        # Nachdem Option 7 abgeschlossen ist, können andere Optionen ausgewählt werden
        print("\n1. Neue Note hinzufügen")
        print("2. Note löschen oder bearbeiten")
        print("3. Schülerdaten anzeigen")
        print("4. Schülerdaten sortieren")
        print("5. Statistik anzeigen")
        print("6. Schülerdaten exportieren")
        print("8. Programm beenden")
        print("9. Schülerdaten aller anzeigen")
        choice = input("\nWählen Sie eine Option (1-9): ")

        # Neue Note hinzufügen
        if choice == "1":
            schuelernummer = input("Schülernummer eingeben: ")
            # Überprüfe, ob die Schülernummer im Schüler-Daten-Dictionary existiert
            if schuelernummer in schueler_dict:
                fachname = input("Fach eingeben: ")
                art = input(
                    "Art der Note (S für Schulaufgabe, M für Mitarbeit, A für Abfrage, E für Extemporale): ")
                try:
                    validate_note_type(art)
                    note = int(input("Note eingeben: "))
                    # Überprüfe, ob das eingegebene Fach im Schüler-Daten-Dictionary existiert
                    if fachname in schueler_dict[schuelernummer].faecher:
                        fach = schueler_dict[schuelernummer].faecher[fachname]
                        fach.add_note_to_fach(art, note)
                    else:
                        raise ValueError(f"Fach {fachname} nicht gefunden.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Schüler {schuelernummer} nicht gefunden.")
        # 2 Note löschen oder bearbeiten
        elif choice == "2":
            # Benutzer wird nach der Schülernummer gefragt
            schuelernummer = input("Schülernummer eingeben: ")
            if schuelernummer in schueler_dict:
                schueler = schueler_dict[schuelernummer]
                # Benutzer gibt das Fach ein
                fachname = input("Fach eingeben: ")
                if fachname in schueler.faecher:
                    fach = schueler.faecher[fachname]
                    print("Noten:")
                    fach.display_grades()
                    try:
                        # Benutzer gibt den Index der zu bearbeitenden/löschenden Note ein
                        index_str = input("Index der zu bearbeitenden/löschenden Note eingeben: ")
                        index = int(index_str) - 1
                        action = input("Möchten Sie die Note bearbeiten (B), löschen (L) oder abbrechen (A)? ").lower()
                        if action == 'b':
                            new_note = int(input("Neue Note eingeben: "))
                            fach.edit_or_delete_note(index, new_note)
                        elif action == 'l':
                            fach.edit_or_delete_note(index)
                        elif action != 'a':
                            raise ValueError(
                                "Ungültige Aktion. Bitte geben Sie 'B' zum Bearbeiten, 'L' zum Löschen oder 'A' zum Abbrechen ein.")
                    except ValueError as e:
                        print(e)
                else:
                    print(f"Fach {fachname} nicht gefunden.")
            else:
                print(f"Schüler {schuelernummer} nicht gefunden.")
        # 3 Schülerdaten anzeigen
        elif choice == "3":
            # Benutzer wird nach der Schülernummer gefragt
            schuelernummer = input("Schülernummer eingeben: ")
            if schuelernummer in schueler_dict:
                schueler_dict[schuelernummer].display_student_grades()
            else:
                print(f"Schüler {schuelernummer} nicht gefunden.")
        # 4 Schülerdaten sortieren
        elif choice == "4":
            sort_option = input("Nach welchem Kriterium möchten Sie sortieren (Vorname, Nachname, Schülernummer)?")
            if sort_option.lower() == "vorname":
                # Sortieren nach dem Vornamen
                schueler_dict = dict(sorted(schueler_dict.items(), key=lambda x: x[1].vorname))
            elif sort_option.lower() == "nachname":
                # Sortieren nach dem Nachnamen
                schueler_dict = dict(sorted(schueler_dict.items(), key=lambda x: x[1].nachname))
            elif sort_option.lower() == "schülernummer":
                # Sortieren nach der Schülernummer
                schueler_dict = dict(sorted(schueler_dict.items(), key=lambda x: x[0]))
            else:
                print("\nUngültiges Sortierkriterium.")
        # 5 Statistik anzeigen
        elif choice == "5":
            # Berechnen der Gesamtnoten und Schüler pro Fach
            gesamtnoten, schueler_pro_fach = berechne_statistikdaten(schueler_dict)
            # Anzeigen der Statistikdaten
            anzeigen_statistikdaten(gesamtnoten, schueler_pro_fach)
        # 6 Schülerdaten exportieren
        elif choice == "6":
            # Benutzer gibt den Dateinamen für den Export ein
            export_path = input(
                "Dateinamen für den Export ein (Beachte, dass Dateiname nur mit .txt oder .docx enden kann): ")
            exportiere_schuelerdaten(schueler_dict, export_path)
        # 8 Programm beenden
        elif choice == "8":
            break
        # 9 Schülerdaten aller anzeigen
        elif choice == "9":
            # Alle Schülerdaten anzeigen
            for schuelernummer, schueler in schueler_dict.items():
                schueler.update_durchschnittsnote()  # Aktualisiere Durchschnittsnoten
                schueler.display_student_grades()


def main():
    schueler_dict = {}
    display_welcome_banner()
    user_interface(schueler_dict)


if __name__ == "__main__":
    main()
