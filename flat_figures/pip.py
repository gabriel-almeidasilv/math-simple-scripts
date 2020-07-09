"""
Área do paralelepípedo
Ab = a * b
At = 2ab + 2bc + 2ac
V  = a * b * c
"""
a = int(input("ArestaA: "))
b = int(input("ArestaB: "))
c = int(input("ArestaC: "))
area_base  = a * b
area_total = ((2 * a * b) + (2 * b * c) + (2 * a * c))
volume     = a * b * c
print("Área da base: {}".format(area_base))
print("Área Total: {}".format(area_total))
print("volume: {}".format(volume))
