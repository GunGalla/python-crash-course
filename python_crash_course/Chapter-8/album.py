# Упражнение 8.7

def make_album(musician, album, traks=None):
    if traks:
        return {'author': musician, 'songs': album, 'num_of_tracks': traks}
    else:
        return {'author': musician, 'songs': album}


print(make_album('Linkin Park', 'Catalyst', 2))
