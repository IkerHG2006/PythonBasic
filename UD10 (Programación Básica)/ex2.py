def comprovar_edat(edat):
   if edat > 18:
       return "Ets major d'edat."
   elif edat < 18:
       return "No ets major d'edat."
   else:
       return "Tens exactament 18 anys."


def edat_usuario():
   edat = int(input("Introdueix la teva edat: "))
   resultat = comprovar_edat(edat)
   print(resultat)


edat_usuario()