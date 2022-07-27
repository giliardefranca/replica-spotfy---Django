from .models import Album

def Romance(requests):
    romance = Album.objects.filter(categoria='ROMANCE')
    return {'romance': romance}


def Sertanejo(requests):
    romance = Album.objects.filter(categoria='SERTANEJO')
    return {'sertanejo': romance}


def Pop(requests):
    romance = Album.objects.filter(categoria='POP')
    return {'pop': romance}


def Forro(requests):
    romance = Album.objects.filter(categoria='FORRO')
    return {'forro': romance}

def Funk(requests):
    romance = Album.objects.filter(categoria='FUNK')
    return {'funk': romance}

def Internacional(requests):
    romance = Album.objects.filter(categoria='INTERNACIONAL')
    return {'internacional': romance}

def Brasil(requests):
    romance = Album.objects.filter(categoria='BRASIL')
    return {'brasil': romance}