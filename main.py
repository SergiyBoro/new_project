name = input("Iveskite savo varda ")
surname = input("Iveskite savo pavarde ")
age = int(input("Iveskite savo amziu "))

vip ={"Antanas": "Kazlauskas", "Vygintas": "Aliukonis", "Simas": "Anriukonis"}


if age >= 21:
    if name in vip and vip[name] == surname:
        print(f"Sveiki, {name}. Jums paruostas V.I.P staliukas")
    else:
         print(f"Sveiki, {name}")

elif age < 0:
    print("Amzius negali buti neigiamas")

else:
    print ("Jusu amzius netinkamas")