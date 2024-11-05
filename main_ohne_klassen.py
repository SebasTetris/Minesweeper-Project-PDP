
import random 

def print_board(board):
    """
    Diese Funktion zeichnet das angegebene Board auf der Konsole.
    Args:
        board (list of list of str): 
        Das Spielbrett, eine 2D-Liste, die den aktuellen Zustand jedes Feldes enthält.
        Die Felder können eine Mine ('💣'), eine Flagge ('🚩'), eine Zahl (die angibt, die viele Minen sich in den angrenzenden Feldern befinden) oder ein Leerzeichen sein, 
        wenn das Feld noch nicht aufgedeckt wurde.
    """
    # Bestimme die Größe des Spielbretts anhand der Länge der ersten Zeile. 
    # Dies setzt voraus, dass das Spielbrett quadratisch ist.
    n = len(board[0])

    # Kopfzeile des Spiels, gibt den Namen des Spiels in der Konsole aus.
    print("\n\t\t\tMINESWEEPER\n")

    # Initialisiere den String für die Spaltenköpfe, beginnend mit einigen Leerzeichen für die Ausrichtung.
    col_header = '    '
    # Initialisiere die horizontale Linie, die unter den Spaltenköpfen und zwischen den Reihen des Bretts gezeichnet wird.
    hline = '   |'

    # Erstelle die Kopfzeile der Spalten und die horizontale Linie durch Iteration über die Anzahl der Spalten.
    for c in range(n):
        # Füge der Kopfzeile die Spaltennummer hinzu, zentriert in einem 4 Zeichen breiten Feld.
        col_header += f" {c:^4} "
        # Füge der horizontalen Linie eine Trennung hinzu.
        hline += '-----|'

    # Drucke die Kopfzeile der Spalten.
    print(col_header)

    # Für jede Reihe im Spielbrett:
    for r in range(n):
        # Drucke die horizontale Linie oberhalb der Reihe.
        print(hline)
        
        # Initialisiere einen leeren String für die aktuelle Reihe.
        row = ''
        # Iteriere über jede Zelle in der Reihe.
        for c in range(n):
            # Wenn die Zelle eine Mine oder eine Flagge enthält, zentriere das Symbol in einem 4 Zeichen breiten Feld.
            # Dies ist notwendig, da Emojis in der Konsole manchmal als zwei Zeichen breit angesehen werden und das Alignment sonst verloren gehen könnte.
            if board[r][c] == '💣' or board[r][c] == '🚩':
                row += f"{board[r][c]:^4}|"
            # Für alle anderen Zellen (Zahlen oder Leerzeichen) verwende ein 5 Zeichen breites Feld zur Zentrierung.
            else:
                row += f"{board[r][c]:^5}|"

        # Drucke die aktuelle Reihe mit der Reihennummer am Anfang.
        print(f" {r} |{row}")

    # Drucke die horizontale Linie unterhalb der letzten Reihe.
    print(hline)




def print_instructions():
    """
    Gibt die Anweisungen auf der Konsole aus.
    """
    print("Anweisungen:")
    print("1. Gib die Reihe und die Spalte an, z.B. '2 3'")
    print("2. Um eine Flage zu setzten, gib noch ein 'F' ein, z.B. '2 3 F'")




def check_victory(b, real_values, displayed_values):
    """
    Diese Funktion checkt, ob man gewonnen hat, indem alle Felder ohne Bomben aufgedeckt wurden oder diese keine Bombe als Nachbar haben.

    Args:
        b (int): 
        Die Gesamtanzahl der Bomben auf dem Spielbrett.
        
        real_values (list of list of int/str): 
        Eine 2D-Liste, die die tatsächlichen Werte der Zellen enthält. 
        Dies kann eine Zahl (die Anzahl der angrenzenden Minen), eine Mine ('💣') oder 
        ein leeres Feld sein, wenn es keine angrenzenden Minen gibt.
        
        displayed_values (list of list of str): 
        Eine 2D-Liste, die darstellt, welche Zellen dem Spieler bereits angezeigt wurden. 
        Dies kann eine aufgedeckte Zahl, eine Flagge ('🚩') oder ein leeres Feld sein.

    Returns:
        bool: Gibt True zurück, wenn der Spieler gewonnen hat, andernfalls False.
    """
    # Bestimme die Größe des Spielbretts anhand der Länge der ersten Zeile der real_values.
    n = len(real_values[0])

    # Initialisiere einen Zähler für die Anzahl der korrekt aufgedeckten Felder.
    count = 0

    # Durchlaufe jede Zelle des Spielbretts.
    for r in range(n):
        for c in range(n):
            # Zählt, ob eine Nicht-Mine korrekt aufgedeckt wurde
            if displayed_values[r][c] != ' ' and displayed_values[r][c] != '🚩':
                count += 1

        # Überprüft, ob alle Nicht-Minen aufgedeckt wurden
    if count == n * n - b:
        return True
    else:
        return False


def generate_board_with_bombs(n, b):
    """
    Diese Funktion initialisiert ein Board mit n Zeilen und Spalten und b Bomben.
    Args:
        n (int): Die Größe des Spielbretts (Anzahl der Zeilen und Spalten). Das Brett ist quadratisch.
        b (int): Die Anzahl der Bomben, die auf dem Brett platziert werden sollen.

    Returns:
        board (list of list of str): Das initialisierte Spielbrett als 2D-Liste.
    """
    # Erstelle eine flache Liste aller Zellen des Spielbretts. 
    # Anfangs sind alle Zellen leer (repräsentiert durch 0).
    cells = [0 for i in range(n*n)]

    # Platziere die Bomben an den Anfang der Liste. 
    # Die ersten 'b' Positionen in der Liste werden mit '💣' markiert, um Bomben darzustellen.
    for i in range(b):
        cells[i] = '💣'

    # Mische die Liste, um die Bomben zufällig auf dem Spielbrett zu verteilen.
    random.shuffle(cells)

    # Initialisiere das 2D-Spielbrett mit leeren Feldern (' ').
    # Dies schafft die Struktur des Spielbretts, in die wir die gemischten Zellen einfügen werden.
    board = [[' ' for i in range(n)] for j in range(n)]

    # Fülle das 2D-Spielbrett mit den Werten aus der gemischten Liste.
    # Die Umwandlung von der flachen Liste in ein 2D-Array ermöglicht die Darstellung des Spielbretts in Minesweeper.
    for i in range(n):
        for j in range(n):
            # Die Zuweisung erfolgt basierend auf der umgerechneten Indexposition.
            # 'i + j*n' berechnet den entsprechenden Index in der flachen Liste für die Position (i, j) im 2D-Array.
            board[i][j] = cells[i + j*n]

    # Rückgabe des initialisierten Spielbretts.
    return board
    # Ein Beispiel für die Umwandlung einer flachen Liste in ein 2D-Array ist im Kommentar unten gezeigt:
    # [0, 1, 2, 3, 4, 5, 6, 7, 8] wird zu [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # wobei jeder Index in der flachen Liste seiner Position im 2D-Array entspricht.
    '''
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ==>
      0  1  2    i/j
    -------------|
    [[0, 1, 2],  | 0   
     [3, 4, 5],  | 1
     [6, 7, 8]]  | 2

    Index 0 in 0,0
    Index 3 in 1,0  
    Index 5 in 1,2
    Index 8 in 2,2

    '''

def generate_values(board):
    """
    Generiert Werte für ein gegebenes Spielfeld, basierend auf der Position von Bomben.

    Die Funktion durchläuft jede Zelle des Spielfelds und erhöht den Wert der Zelle um 1 für jede benachbarte Bombe.
    Die Funktion überspringt Zellen, die eine Bombe enthalten.

    Args:
        board (list of list of str/int): 
        Das Spielbrett, auf dem die Werte generiert werden sollen.
        Bomben sind als '💣' gekennzeichnet, leere Felder zunächst mit 0.

    Returns:
        list of list of int: 
        Das aktualisierte Spielbrett mit den generierten Werten für jede Zelle.
    """  

    # Bestimme die Größe des Spielbretts (angenommen, es ist quadratisch).
    n = len(board[0])

    # Durchlaufe jede Zelle des Spielbretts, um die Anzahl der angrenzenden Minen zu berechnen.
    for row in range(n):
        for col in range(n):
 
            # Überspringe die Berechnung für Zellen, die eine Bombe enthalten.
            if board[row][col] == '💣':
                continue
                    
            # Überprüfe die Zelle direkt oberhalb.
            if row > 0 and board[row-1][col] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle oben links.
            if row > 0 and col > 0 and board[row-1][col-1] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle oben rechts.
            if row > 0 and col < n-1 and board[row-1][col+1] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle direkt unterhalb.
            if row < n-1  and board[row+1][col] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle unten links.
            if row < n-1 and col > 0 and board[row+1][col-1] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle unten rechts.
            if row < n-1 and col < n-1 and board[row+1][col+1] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle direkt links.
            if col > 0 and board[row][col-1] == '💣':
                board[row][col] += 1

            # Überprüfe die Zelle direkt rechts.
            if col < n-1 and board[row][col+1] == '💣':
                board[row][col] += 1

    # Gebe das aktualisierte Spielbrett mit den berechneten Werten zurück.
    return board

def start():
    """
    Startet das Spiel "Minesweeper".
    Diese Funktion initialisiert das Spielfeld, platziert Bomben zufällig und berechnet die Werte für jede Zelle basierend auf der Anzahl der benachbarten Bomben.
    Anschließend führt sie den Spielzyklus aus, in dem der Spieler Eingaben macht, um Zellen zu enthüllen oder Flaggen zu platzieren.
    Das Spiel endet, wenn der Spieler auf eine Bombe trifft oder alle sicheren Zellen enthüllt hat.
    """
 # Initialisiere die Spielgröße und die Anzahl der Bomben.
    n = 6       # Definiert die Größe des Spielbretts als 6x6 Felder.
    b = 8   # Legt fest, dass 8 Bomben zufällig auf dem Spielbrett platziert werden.
    flags = []  # Eine leere Liste, um die Positionen der gesetzten Flaggen zu speichern.

    # Initialisiere die Listen, die die Werte auf dem Spielbrett speichern.
    real_values = []  
    # Diese Liste wird später mit den echten Werten (Bomben und Zahlen) gefüllt.
    displayed_values = [[' ' for y in range(n)] for x in range(n)]  
    # Zeigt anfänglich leere Felder an.

    # Initialisiere das Spielbrett mit Bomben und berechne die Werte für jede Zelle.
    real_values = generate_board_with_bombs(n, b)  # Platziere Bomben zufällig auf dem Brett.
    real_values = generate_values(real_values)  # Berechne die Zahlen für jede Zelle basierend auf den benachbarten Bomben.

    print_board(real_values)  
    # Zeige das Spielbrett im Testmodus an, um die Platzierung der Bomben zu sehen.

    print_instructions()  
    # Zeige die Anweisungen für den Spieler an.

    # Spiel-Hauptschleife beginnt hier.
    game_over = False  
    # Eine Variable, um den Spielstatus zu überwachen.
    while not game_over:
        print_board(displayed_values)  # Zeichne das Spielbrett für den Spieler bei jedem Durchlauf neu.

        try: 
            # Fordere Spielerinput an und überprüfe die Gültigkeit der Eingabe.
            inp = input("\nGib die Reihe und die Spalte an: ").split()
            r, c = int(inp[0]), int(inp[1])  # Konvertiere Eingaben in Integer.
            
            # Überprüfe, ob die eingegebenen Koordinaten innerhalb des gültigen Bereichs liegen.
            assert r >= 0 and r < n and c >= 0 and c < n
            # Stelle sicher, dass das gewählte Feld entweder leer oder mit einer Flagge markiert ist.
            assert displayed_values[r][c] == ' ' or displayed_values[r][c] == '🚩'
            
            # Behandle das Setzen oder Entfernen von Flaggen basierend auf der Eingabe.
            # FLAGS
            if len(inp) == 3:

                # Eingegebener Buchstabe ist ein 'F' und die Flage existiert noch nicht
                assert inp[2].lower() == 'f' 
        except Exception:
            print("Falscher Input! Versuche es nochmal!\n")
            print_instructions()
            continue
        

        # Wenn wir uns im Flag Mode bedinden, dann Flage hinzufügen oder entfernen.
        if len(inp) == 3:
            
            if (r,c) not in flags:
                # Eine neue Flage setzen (als Tupel von Row und Column)
                flags.append((r,c))
                    
                # Die Flage auf dem Board zeigen
                displayed_values[r][c] = '🚩'

                print(f'Flag {(r,c)} hinzugefügt!')

            # Sollte die ausgewählte Position eine vordefiniert Flage sein, dann entferne die Flage
            else:
                # Die Flage entfernen (als Tupel)
                flags.remove((r,c))                

                # Die Flage aus dem Board entfernen
                displayed_values[r][c] = ' '

                print(f'Flag {(r,c)} wurde entfernt!')
    
        # Sollte die ausgewählte Position eine Bombe sein, dann GAME OVER
        elif real_values[r][c] == '💣':

            # Zeige die Bombe auf der Konsole
            displayed_values[r][c] = '💣'

            print_board(displayed_values)

            print("GAME OVER!!!")

            game_over = True

        # Sollte die ausgewählte Position KEINE Bombe sein, dann zeige den echten Wert der Zelle
        else:
            displayed_values[r][c] = real_values[r][c]

        # Sollten alle Felder endetckt sein, dann GEWONNEN
        if check_victory(b, real_values, displayed_values):

            print_board(displayed_values)

            print("Du hast gewonnen!!!")

            game_over = True

start()


