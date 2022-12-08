# Упражнение 8.8
from album import make_album

while True:
    print('\nPlease, enter album information: ')
    print('(press "q" to quit any time)')

    musician = input('Enter musician name: ')
    if musician == 'q':
        break

    album = input('Enter album name: ')
    if album == 'q':
        break

    track = input('Enter number of tracks in album: ')
    if track == 'q':
        break

    formatted_album = make_album(musician, album, track)
    print(formatted_album)
