from sympy import primerange

# Générer les 100 premiers nombres premiers à partir de 31
nb_premiers = list(primerange(31, 602))

# Listes d'amplitudes, fréquences et phases
amplitudes = list(primerange(31, 602))[::-1]  # Inverser l'ordre des nombres premiers
frequences = list(primerange(1009, 1722))
phases = list(primerange(2, 542))

# Fonction pour générer un sinus
def generer_sinus(index, amplitude, frequence, phase):
    return f"#define SINE{index} {amplitude}*sin({frequence}*x+6.28/{phase})"

# Génération de chaque sinus
sine_codes = [generer_sinus(i+1, amplitude, frequence, phase) for i, (amplitude, frequence, phase) in enumerate(zip(amplitudes, frequences, phases))]

# Affichage de la somme des sinus
#print("#define POLY(x)", end=" ")
print(sine_codes[0], end="\n")
for sine_code in sine_codes[1:]:
    print(f"{sine_code}", end="\n")
print()
