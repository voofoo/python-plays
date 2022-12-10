import random
import time

def introText():
    print('''Είσαι στη Χώρα του GovΤελείαGR. Παντού κυκλοφορούν Θεματοφύλακες Του Συντάγματος
και γράφουν πρόστιμα σε όποιον δεν έχει πιστοποιημένο πιστοποιητικό Πιστοποίησης''')
    print('''Μπροστα σου βλέπεις μια έρημη και σκοτεινή διασταύρωση...''')
    print()

def pathChoice():
    choice = ''
    while choice != '1' and choice != '2':
        print('Απο πού θα πας, απο εδώ ή απο εκεί ? (1 or 2)')
        choice = input()

    return choice

def checkPath(chosenPath):
    print('Κάνεις δύο βήματα και κοιτάς απο δώ...')
    time.sleep(2)
    print('Δε φαίνεται κανείς...')
    time.sleep(2)
    print('Κάνεις δύο βήματα και κοιτάς απο κεί...')
    time.sleep(2)
    print('Δε κουνιέται φύλλο...')
    time.sleep(2)
    print('Κάνεις το πρώτο βήμα και τσουπ!! Ένας Θεματοφύλακας του Συντάγματος περνά απο μπροστά σου...')
    print()
    time.sleep(2)

    friendlyPath = random.randint(1, 2)

    if chosenPath == str(friendlyPath):
         print('Κοιτά με θαυμασμό τις πεταλούδες και δε σε είδε! Τη γλίτωσες!!')
    else:
         print('Σε τσάκωσε να κυκλοφορείς χωρίς πιστοποιημένο πιστοποιητικό Πιστοποίησης! Θα σου γραψει πρόστιμο...')

wannaPlay = 'yes'
while wannaPlay == 'yes' or wannaPlay== 'y':
    introText()
    choiceNumber = pathChoice()
    checkPath(choiceNumber)

    print('Θες να δοκιμάσεις να ξαναβγεις χωρίς πιστοποιητικό ? (yes or no)')
    wannaPlay = input()
