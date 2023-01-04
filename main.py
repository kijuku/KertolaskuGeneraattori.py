def TulostaKertotaulu(luku):
  for x in range(1, 11):
    if x < 0:
      print(luku, "* (", x, ") =", luku * x)
    else:
      print(luku, "*", x, "=", luku * x)
  return None


def paaohjelma():
  print("Kertotaulu")
  for x in range(-11, 11):
    if x < 0:
      print("8 * (", x, ") =", 8 * x)
    else:
      print("8 *", x, "=", 8 * x)
  
  while True:
    luku = int(input("Anna luku:"))
    print("Tulostan luvun",luku,"kertotaulun:")
    TulostaKertotaulu(luku)
    print("")
    if luku == 0:
      print("Kiitos kun käytit ohjelmaa.")
      break

  

  
  luku = 1
  print("Kertotaulu ", luku, ": ")
  TulostaKertotaulu(luku)
  luku = 9
  print("Kertotaulu ", luku, ": ")
  TulostaKertotaulu(luku)
  luku = -13
  print("Kertotaulu ", luku, ": ")
  TulostaKertotaulu(luku)


paaohjelma()
