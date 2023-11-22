---

marp: true
theme: gaia
class: lead
paginate: true
_backgroundImage: url('./1.png')

---
---

<!-- backgroundImage: url('./50_b_w.png') -->

# 1. Les Variables

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Une variable est une manière de stocker une donnée. La variable doit avoir un type pour définir la donnée stockée.

Les types possibles sont:
- int => Chiffre ou nombre
- str => Caractère ou chaîne de caractères
- bool => Boolean True ("Vrai") ou False ("Faux")
- ...

---

# Exemple:

```python
un_bool = True
un_int = 42
une_str = "Coucou"

print("Ceci est un boolean:", un_bool)
print("Ceci est un integer:", un_int)
print("Ceci est une chaine de caracteres:", une_str)
```

---

# 2. Les fonctions

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Les fonctions définissent des actions à faire lors de leur appel.
Une fonction est constituée de son nom, des paramètres pris en entrée et de son type de retour.

---

# Exemple:

```python
# Cette fonction affiche "bonjour"
def afficher_bonjour():
    print("Bonjour")

# Cette fonction affiche le contenu de mot
def afficher_argument(mot="Salut"):
    print(mot)

# Cette fonction affiche "Coucou" et renvoi le même mot
def afficher_et_renvoyer_coucou() -> str:
    mot = "Coucou"
    print(mot)
    return mot

def main():
    afficher_bonjour()
    afficher_argument("Bonjour à tous, je suis un argument")
    afficher_argument()
    retour = afficher_et_renvoyer_coucou()
    print("retour =", retour)
```

---

# 3. Les conditions

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Les conditions permettent de limiter l'exécution d'une action si et seulement si la condition est valide.

---

# Exemple:

```python
def positif_ou_negatif(nombre: int):
    if nombre > 0:
        print(nombre, "est positif !")
    else:
        print(nombre, "est negatif !")
```

---

# 4. Les Boucles

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Les boucles sont des éléments qui permettent de répéter une action, un nombre de fois définit par la condition d'arrêt.

---

# Exemple:

```python
def dire_bonjour_a_tous_les_etudiants(nombre_etudiants: int):
    indice = 1
    while indice <= nombre_etudiants:
        print("Bonjour etudiant numero", indice, "\n")
        indice = indice + 1
```

---

# 5. Les Class

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Les class sont des structures de code qui définissent un objet et les comportements qu'il peut réaliser.
Comme dans l'exemple suivant, vous pouvez importer une class "Robot" depuis la bibliothèque "Robot". 
Ensuite, il vous faut créer un objet Robot, avec ici un nom et un âge.
Par la suite, vous pouvez donner des ordres à votre robot, en faisant appel aux méthodes que la class Robot contient.

---

# Exemple:

```python {.line-numbers}
from pybot import Robot


def main():
    robot = Robot("Nono", 11)
    robot.dire_bonjour()
    robot.rendre_muet()
    robot.dire_bonjour()
    robot.donner_la_parole()
    robot.dire_bonjour()
```


---

# 6. La bibliothèque Pybot

---

<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') -->

Pybot est une bibliothèque avec une Class Robot que l'on peut utiliser pour faire un programme graphique.

Voici présenté ici les méthodes et des exemples d'utilisation:

---

---

---