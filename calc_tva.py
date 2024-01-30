

produs = input("Produs (orez, apa, fructe etc)(UN PRODUS PER INPUT): ").lower()
tip = input("Tip (alimentar / nealimentar): ").lower()
categorie = input("Categorie (aliment, bauturi[CU EXCEPTIE APA, LAPTE], 0 [DACA ESTE NEALIMENTAR]): ").lower()
pret = input("Pret: ")


def tva_calc(produs,tip,categorie, pret):
  if tip == "alimentar" and categorie == "aliment":
    tva = round(pret * 9/100,2)
    print("\n{} are adaugat TVA in valoare de {}".format(produs.upper(), tva))
    pret_fara_tva = pret - tva
    print(round(pret_fara_tva,2))
    print("Pret fara TVA: "+ str(pret_fara_tva)+"\nPret integral: "+ str(pret))
  elif tip == "alimentar" and categorie == "bauturi":
    tva = round(pret * 19/100,2)
    print("\n{} are adaugat TVA in valoare de {}".format(produs.upper(), tva))
    pret_fara_tva =round(pret - tva,2)
    print("Pret fara TVA: "+ str(pret_fara_tva)+"\nPret integral: "+ str(pret))
  elif tip == "nealimentar" and categorie == 0 or categorie == "0":
    tva = round(pret * 19/100,)
    print("\n{} are adaugat TVA in valoare de {}".format(produs.upper(), tva))
    pret_fara_tva =round(pret - tva,2)
    print("Pret fara TVA: "+ str(pret_fara_tva)+"\nPret integral: "+ str(pret))

tva_calc(produs, tip, categorie, float(pret))
