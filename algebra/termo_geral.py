"""
General term for PA (Aritimethics progressions)
 a1, a2, a3, a4, a5, ... An = a1 (n - 1) * r
"""
#PA input datas
PA = [1, 4, 7, 10]
print("PA={}".format(PA))

def calcGeneralTerm():
	#general term formula
	tAn    = int(input("find an: "))
	reason = int(input("reason: "))
	an     = PA[0] + (tAn - 1) * reason
	print("General term is = {}".format(an))

#main function
def main():
	calcGeneralTerm()

if __name__ == "__main__":
	main()
