giris=input("Please enter a sentence you want to make an acronym from: ")
def acronym_maker(cuumle):
    sonuc=""
    cumle=cuumle.split()
    for i in cumle:
        sonuc+=i[0]
    return sonuc.upper()            
print(acronym_maker(giris))