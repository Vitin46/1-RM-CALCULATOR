
#FORMULA GERAL: carga × (36 / (37 – numero de reps))

#AGACHO: CARGA / 1,03 - (0.03 * REPS)
#SUPINO: CARGA / 1,0278 - (0,03 * REPS)
#TERRA: CARGA * (1 + 0.0333 * REPS)
while True:
    print("CALCULE SEU 1 RM!!")
    print("ESCOLHA QUAL LIFT DESEJA CALCULAR")

    lift = int(input("(1) AGACHO   (2) SUPINO  (3) TERRA "))


    if lift == 1:
        carga1 = float(input("DIGITE A CARGA LEVANTADA EM KG: "))
        reps1 = int(input("DIGITE O NUMERO DE REPS FEITAS: "))
        calculo1 = 1.03 - (0.03 * reps1)
        rmAgacho = carga1 / calculo1
        rmAgachoArredondado = round(rmAgacho, 2)
        print("SEU RM NO AGACHO É: ", rmAgachoArredondado, "KG!!!")

    elif lift == 2:
        carga2 = float(input("DIGITE A CARGA LEVANTADA EM KG: "))
        reps2 = int(input("DIGITE O NUMERO DE REPS FEITAS: ")) 
        calculo2 = 1.0278 - (0.03 * reps2)
        rmSupino = carga2 / calculo2
        rmSupinoArredondado = round(rmSupino, 2)
        print("SEU RM NO SUPINO É: ", rmSupinoArredondado, "KG!!!")

    elif lift == 3:
        carga3 = float(input("DIGITE A CARGA LEVANTADA EM KG: "))
        reps3 = int(input("DIGITE O NUMERO DE REPS FEITAS: "))
        rmTerra = carga3 * (1 + 0.0333 * reps3)
        rmTerraArredondado = round(rmTerra, 2)
        print("SEU RM NO TERRA É: ", rmTerraArredondado, "KG!!!")

    else:
        print("opção inexistente.")
        break