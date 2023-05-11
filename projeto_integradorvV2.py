from getpass import getpass
from mysql.connector import connect, Error

def executarSelect(query):
    try:
        with connect(
            host="us-cdbr-east-06.cleardb.net",
            user="b5390412538351",
            password="e827f4fc",
            database="heroku_a8dd37572b9035f"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
                #cursor.execute(query)
                #connection.commit()
    except Error as e:
        print(e)

def executarInsert(query):
    try:
        with connect(
            host="us-cdbr-east-06.cleardb.net",
            user="b5390412538351",
            password="e827f4fc",
            database="heroku_a8dd37572b9035f"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                return True
    except Error as e:
        print(e)
        return False
        
resultado = executarSelect('select * from amostras')
#print(resultado)

def NumeroNatural(natural):
    while True: 
        try:         
            num=float(input(natural))
        except:
            print("O numero deve ser maior que zero, tente novamente!")
        else:
            if num>=0: return num
            print("O numero deve ser maior que zero, tente novamente!")


def qualificacao():
                mp10 = NumeroNatural("Digite o valor das particulas inaláveis: ")
                mp25=NumeroNatural("Digite o valor das particulas finas: ")
                o3= NumeroNatural("Digiite o valor do ozonio: ")
                co=NumeroNatural("Digite o valor do monoxido de carbono: ")
                no2=NumeroNatural("Digite o valor do dioxido de nitrogenio: ")
                so2=NumeroNatural("Digite o valor do dioxido de enxofre: ")
           

                
     
                if mp10 < 51 and mp25 < 26 and o3 < 101 and co < 10 and no2 < 201 and so2 < 21:
                    qualidade = "BOA." 
                    print("A qualidade do ar é", qualidade, "não há efeito a saúde.")
                
                elif mp10 <= 100 and mp25 <=50 and o3 <=130 and co <=11 and no2 <=240 and so2 <=40:
                    qualidade = "MODERADA."
                    print("A qualidade do ar é", qualidade,)
                    print("Os efeitos na saúde são:")
                    print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratônias e cardiacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
                    
                elif mp10 <= 150 and mp25 <=75 and o3 <=160 and co <=13 and no2 <=320 and so2 <=365:
                    qualidade = "RUIM."
                    print("A qualidade do ar é,", qualidade,) 
                    print("Os efeitos na saúde são:")
                    print("Toda a população pode apresentar sintomas como fosse seca, cansaço,ardor nos olhos, nariz e garganta, Pessoas de grupos sensiveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas) podem apresentar efeitos mais sérios na saude")
                    
                elif mp10 <= 250 and mp25 <=125 and o3 <=200 and co <=15 and no2 <=1130 and so2 <=800:
                    qualidade = "MUITO RUIM."
                    print("A qualidade do ar é", qualidade,)
                    print("Os efeitos na saúde são:")
                    print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas).")
                    
                elif mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800:
                    qualidade = "PÉSSIMA."
                    print("A qualidade do ar é", qualidade,)
                    print("Os efeitos na saúde são:")
                    print("Toda a população pode apresentar sérios riscos de manfestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis.")
             



qualificacao()