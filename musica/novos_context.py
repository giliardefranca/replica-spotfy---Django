from .models import Album

def Romance(requests):
    romance = Album.objects.filter(categoria='ROMANCE')
    return {'romance': romance}


def Sertanejo(requests):
    sertanejo = Album.objects.filter(categoria='SERTANEJO')
    return {'sertanejo': sertanejo}


def Pop(requests):
    pop = Album.objects.filter(categoria='POP')
    return {'pop': pop}


def Forro(requests):
    forro = Album.objects.filter(categoria='FORRO')
    return {'forro': forro}

def Funk(requests):
    funk = Album.objects.filter(categoria='FUNK')
    return {'funk': funk}

def Internacional(requests):
    internacional = Album.objects.filter(categoria='INTERNACIONAL')
    return {'internacional': internacional}

def Brasil(requests):
    brasil = Album.objects.filter(categoria='BRAZIL')
    return {'brasil': brasil}