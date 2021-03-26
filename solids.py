from math import pi

def cube():
    arete = int(input("Entrez une arête du cube (en cm) :"))
    result = arete * arete * arete

    print(arete, "×", arete, "×", arete, "=", result)
    print("Le volume de ce cube est", result, "cm" + "\u00B3")

def pave_droit():
    x = int(input("Entrez la largeur du pavé droit (en cm) :"))
    y = int(input("Entrez la longeur du pavé droit (en cm) :"))
    z = int(input("Entrez la profondeur du pavé droit (en cm) :"))
    result = x * y * z
    print(x, "×", y, "×", z, "=", result)
    print("Le volume de ce pavé droit est ", result, "cm" + "\u00B3")

def cone():
    rayon_cone = int(input("Entrez le rayon du cecle de la pyramide (en cm) :"))
    hauteur_cone = int(input(" Entrez la hauteur du cone (en cm) :"))
    result = 1 / 3 * pi * rayon_cone * rayon_cone * hauteur_cone
    print("1 ÷ 3 ×", "π ×", rayon_cone, "×", hauteur_cone, "=", result)
    print("Le volume de ce cone est environ ", result, "cm" + "\u00B3")

def pyramide():
    hauteur_pyramide = int(input("Entrez la hauteur de la pyramide (en cm) :"))
    longeur_base = int(input("Entrez la longeur de la base de la pyramide (en cm) :"))
    largeur_base = int(input("Entrez la largeur de la base de la pyramide (en cm) :"))
    result = 1 / 3 * hauteur_pyramide * longeur_base * largeur_base
    print("1 ÷ 3 ×", hauteur_pyramide, "×", longeur_base, "×", largeur_base, "=", result)
    print("Le volume de cette pyramide est", result, "cm" + "\u00B3")

def cylindre():
    rayon_cylindre = int(input("Entrez le rayon du cercle (en cm) :"))
    hauteur_cylindre = int(input("Entrez la hauteur du cylindre (en cm) :"))
    result = pi * rayon_cylindre * rayon_cylindre * hauteur_cylindre
    print("π ×", rayon_cylindre, "×", rayon_cylindre, "×", hauteur_cylindre, "=", result )
    print("Le volume de ce cylindre est environ ", result, "cm" + "\u00B3")
    
def boule():
    rayon_boule = int(input("Entrez le rayon de la boule (en cm) :"))
    result = 4 / 3 * pi * rayon_boule * rayon_boule * rayon_boule
    rayon_boule_afficher = str(rayon_boule)
    print("4 ÷ 3 x π x", rayon_boule_afficher + "\u00B3")
    print("Le volume de cette boule est environ ", result, "cm" + "\u00B3")

def autre():
    print("Solide invalide !")
    print(" ")

while 1 == 1:
    
    type_solid = input("Quel type de solide voulez-vous calculer (cube, pavé droit, cône, boule, pyramide, cylindre) ? ")

    
    if type_solid == "cube":
        cube()
        pass

    elif type_solid == "pavé droit":
        pave_droit()
        pass

    elif type_solid == "cone" or type_solid == "cône": 
        cone()
        pass
        
    elif type_solid == "boule":
        boule()
        pass

    elif type_solid == "pyramide":
        pyramide()
        pass

    elif type_solid == "cylindre":
        cylindre()
        pass

    else:
        autre()
        
while 1 == 1:
    
    type_solid = input("Quel autre type de solide voulez-vous calculer (cube, pavé droit, cône, boule, pyramide, cylindre) ? ")

    
    if type_solid == "cube":
        cube()

    elif type_solid == "pavé droit":
        pave_droit()

    elif type_solid == "cone" or type_solid == "cône": 
        cone()
        
    elif type_solid == "boule":
        boule()

    elif type_solid == "pyramide":
        pyramide()

    elif type_solid == "cylindre":
        cylindre()

    else:
        autre()
