import time

_HARTA = {
    "Arad":           {"Zerind": 75, "Sibiu": 140, "Timișoara": 118},
    "Zerind":         {"Arad": 75, "Oradea": 71},
    "Oradea":         {"Zerind": 71, "Sibiu": 151},
    "Timișoara":      {"Arad": 118, "Lugoj": 111},
    "Lugoj":          {"Timișoara": 111, "Mehadia": 70},
    "Mehadia":        {"Lugoj": 70, "Drobeta": 75},
    "Drobeta":        {"Mehadia": 75, "Craiova": 120},
    "Craiova":        {"Drobeta": 120, "Râmnicu Vâlcea": 146, "Pitești": 138},
    "Sibiu":          {"Arad": 140, "Oradea": 151, "Făgăraș": 99, "Râmnicu Vâlcea": 80},
    "Râmnicu Vâlcea": {"Sibiu": 80, "Craiova": 146, "Pitești": 97},
    "Făgăraș":        {"Sibiu": 99, "București": 211},
    "Pitești":        {"Râmnicu Vâlcea": 97, "Craiova": 138, "București": 101},
    "București":      {"Făgăraș": 211, "Pitești": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu":        {"București": 90},
    "Urziceni":       {"București": 85, "Hârșova": 98, "Vaslui": 142},
    "Hârșova":        {"Urziceni": 98, "Eforie": 86},
    "Eforie":         {"Hârșova": 86},
    "Vaslui":         {"Urziceni": 142, "Iași": 92},
    "Iași":           {"Vaslui": 92, "Neamț": 87},
    "Neamț":          {"Iași": 87},
}

cereri = [] #log-uri cereri realizate de clienti

def acces_harta(locatie):
    destinatie = _HARTA.get(locatie)
    cereri.append(locatie) #log locatie ceruta
    #simulare cost cerere
    time.sleep(1)
    return destinatie

#definire harta locala
harta_locala = {}

#functie incarcare date primite de la serviciu in harta locala
def incarca(locatia):
    locatie_existenta = harta_locala.get(locatia)
    if locatie_existenta == None:
        harta_locala[locatia] = acces_harta(locatia)
    return harta_locala[locatia]

def resetare():
    harta_locala = {}
    cereri = []

def resetare_harta_locala(harta):
    return {}

def adauga_harta_locala(harta, locatie):
    harta[locatie] = {"Test": {"Nicaieri":100}}

    
#testare agent
print(acces_harta("Iași"))
print(acces_harta("Giurgiu"))
incarca("Iași")
incarca("Timișoara")

print(cereri)
print(harta_locala)

harta_locala = resetare_harta_locala(harta_locala)
adauga_harta_locala(harta_locala,"Paris")

print(harta_locala)

