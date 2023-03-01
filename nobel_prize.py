import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}



# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året


def main():


    while True:
        print(HELP_STRING)
        choice = input (">" ).lower()
        if choice == "a":
            choice_quit()
            print ("BYE")
            break
        elif choice == "h":
            show_help_text()
        else:
            list_input = choice.split()
            if len (list_input) == 1: # just the year
                year = list_input[0]
                category = ""
            elif len (list_input) == 2:
                year, subject = choice.split()
                category = cat [subject]

                search_param =  {"nobelPrizeyear": int(year) , "nobelPrizecategory": category}

                result = requests.get("http://api.nobelprize.org/2.1/nobelprizes", param=search_param).json() # result = dict
                # pprint.pprint(result)
                nobel_prizes(result)


def main():

    while True:
        print(HELP_STRING)
        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        # TODO 5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        aaa = input(">")
        a, b = aaa.split()
        c = cat[b]


        c = {"nobelPrizeYear": int(a),"nobelPrizeCategory":c}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

        # TODO 20p Skapa en funktion som ger en summering av ett år. Om användaren exempelvis skriver "summering 1965"
        #   skall programmet skriva ut den totala prissumman det året samt hur många pristagare det var.
        #   Du skall alltså summera alla priser det året och räkna antalet pristagare.
        #   Exempel på hur det kan se ut:
        #   > summering 1965
        #   År 1965 fick 9 pristagare dela på totalt 1410000 kronor
        #   Tips: Tänk på alla priser inte delats ut alla år. Ekonomipriset infördes exempelvis 1968

        for p in res["nobelPrizes"]:
            peng = p["prizeAmount"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")

            for m in p["laureates"]:
                print(m['knownName']['en'])
                print(m['motivation']['en'])


if __name__ == '__main__':
    main()
