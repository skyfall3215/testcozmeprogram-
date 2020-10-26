import time
print("soru cevap programına hoş geldiniz")

x = str(input("hoş geldiniz başlatmak için 1 yazın: "))

if x == "1":
    print("başlıyor ancak adınızı girmelisiniz.")

else:
    print("1 yazın dedim ama olsun şimdi adınızı gireceksiniz.")

ad = str(input("adınızı girin: "))

print("hadi başlayalım",ad,"!!!")

soru1 = input("""
============================================
1.soru osmanlı devletini kim kurmuştur?
A) orhan bey
B) yıldırım beyazıt
C) osman bey
D) 1.mehmet (çelebi mehmet)
============================================
Cevabınızı giriniz: """)

if soru1 == "C" or soru1 == "c":
    print("doğru cevap")

elif soru1 == "A" or soru1 == "a":
    print("yanlış cevap\ndoğru cevap C")

elif soru1 == "B" or soru1 == "b":
    print("yanlış cevap\ndoğru cevap C")

elif soru1 == "D" or soru1 == "d":
    print("yanlış cevap\ndoğru cevap C")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")


soru2 = input("""
====================================================================================
2.soru osmanlı devletinde ilk gümüş para hangi padişah tarafından kullanılmıştır?
A) osman bey
B) orhan bey
C) fatih sultan mehmet
D) yıldırım beyazıt
====================================================================================
cevabınızı giriniz: """)

if soru2 == "B" or soru2 == "b":
    print("doğru cevap")

elif soru2 == "A" or soru2 == "a":
    print("yanlış cevap\ndoğru cevap B")

elif soru2 == "C" or soru2 == "c":
    print("yanlış cevap\ndoğru cevap B")

elif soru2 == "D" or soru2 == "d":
    print("yanlış cevap\ndoğru cevap B")


else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")


soru3 = input("""
====================================================================
3.soru 6 . ( x + 4 ) + 3 . ( x - 8 ) = 45 olduğuna göre, x kaçtır ?
A) 4
B) 5
C) 6
D) 7
====================================================================

cevabınızı giriniz: """)

if soru3 == "B" or soru3 == "b":
    print("doğru cevap")

elif soru3 == "A" or soru3 == "a":
    print("yanlış cevap\ndoğru cevap B")

elif soru3 == "C" or soru3 == "c":
    print("yanlış cevap\ndoğru cevap B")

elif soru3 == "D" or soru3 == "d":
    print("yanlış cevap\ndoğru cevap B")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru4 = input("""
====================================================================
4.soru nene hatununda savaştığı osmanlı-rus savaşının adı nedir?
A) çanakkale savaşı
B) 1.dünya savaşı
C) 93 harbi
D) kurtuluş savaşı
====================================================================
cevabınızı girin: """)

if soru4 == "C" or soru4 == "c":
    print("doğru cevap")

elif soru4 == "A" or soru4 == "a":
    print("yanlış cevap\ndoğru cevap C")

elif soru4 == "B" or soru4 == "b":
    print("yanlış cevap\ndoğru cevap C")

elif soru4 == "D" or soru4 == "d":
    print("yanlış cevap\ndoğru cevap C")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru5 = input("""
====================================================================
5.soru 1 duvarı 6 işçi boyadığına göre 4 duvarı kaç işçi boyar?
A) 24
B) 45
C) 76
D) 90
====================================================================
cevabınızı girin: """)

if soru5 == "A" or soru5 == "a":
    print("doğru cevap")

elif soru5 == "B" or soru5 == "b":
    print("yanlış cevap\ndoğru cevap A")

elif soru5 == "C" or soru5 == "c":
    print("yanlış cevap\ndoğru cevap A")

elif soru5 == "D" or soru5 == "d":
    print("yanlış cevap\ndoğru cevap A")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru6 = input("""
====================================================================
6.soru Aşağıdaki cümlelerin hangisinde ek fiil yoktur ?
A) Orada kimse kimseye kötülük etmezmiş.
B) Salon ağzına kadar doluydu.
C) Bana, onun parası vardır, dedi.
D) Sen gidedur, ben burada bekleyeceğim.
====================================================================
cevabınızı girin: """)

if soru6 == "D" or soru6 == "d":
    print("doğru cevap")

elif soru6 == "A" or soru6 == "a":
    print("yanlış cevap\ndoğru cevap D")

elif soru6 == "B" or soru6 == "b":
    print("yanlış cevap\ndoğru cevap D")

elif soru6 == "C" or soru6 == "c":
    print("yanlış cevap\ndoğru cevap D")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru7 = input("""
================================================================
7.soru 2.geçen kaçıncı olur?
A) 1.
B) 2.
C) 3.
D) 4.
================================================================
cevabınızı girin: """)

if soru7 == "B" or soru7 == "b":
    print("doğru cevap")

elif soru7 == "A" or soru7 == "a":
    print("yanlış cevap\ndoğru cevap A")

elif soru7 == "C" or soru7 == "c":
    print("yanlış cevap\ndoğru cevap A")

elif soru7 == "D" or soru7 == "d":
    print("yanlış cevap\ndoğru cevap D")

çık = input("oyun bitti. Çıkmak için q tuşuna basın: ")
print("hoşcakal", ad , ":)")

if çık == "q" or çık == "Q":
    print("çıkılıyor...")
    exit()

else:
    print("q tuşuna basın dedim ama olsun.")
    time.sleep(3)
    exit()
