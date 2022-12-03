from difflib import SequenceMatcher


def compare(cf):
    with open(cf) as file0, open("B1.csv") as file1, open("B2.csv") as file2, open("B3.csv") as file3, open("B4.csv") as file4, open("B5.csv") as file5, open("B6.csv") as file6, open("B7.csv") as file7, open("B8.csv") as file8, open("B9.csv") as file9, open("B10.csv") as file10:
        com0 = file0.read()
        com1 = file1.read()
        com2 = file2.read()
        com3 = file3.read()
        com4 = file4.read()
        com5 = file5.read()
        com6 = file6.read()
        com7 = file7.read()
        com8 = file8.read()
        com9 = file9.read()
        com10 = file10.read()

        print("The inserted data is : ", com0)

        sum1 = SequenceMatcher(None, com0, com1).ratio()
        sum2 = SequenceMatcher(None, com0, com2).ratio()
        sum3 = SequenceMatcher(None, com0, com3).ratio()
        sum4 = SequenceMatcher(None, com0, com4).ratio()
        sum5 = SequenceMatcher(None, com0, com5).ratio()
        sum6 = SequenceMatcher(None, com0, com6).ratio()
        sum7 = SequenceMatcher(None, com0, com7).ratio()
        sum8 = SequenceMatcher(None, com0, com8).ratio()
        sum9 = SequenceMatcher(None, com0, com9).ratio()
        sum10 = SequenceMatcher(None, com0, com10).ratio()

        p1 = sum1*100
        p2 = sum2*100
        p3 = sum3*100
        p4 = sum4*100
        p5 = sum5*100
        p6 = sum6*100
        p7 = sum7*100
        p8 = sum8*100
        p9 = sum9*100
        p10 = sum10*100

        print("THE GIVEN FILES MATCHES ", p1, "PERCENT WITH TEXTBOOK ONE\n")
        print("THE GIVEN FILES MATCHES ", p2, "PERCENT WITH TEXTBOOK TWO\n")
        print("THE GIVEN FILES MATCHES ", p3, "PERCENT WITH TEXTBOOK THREE\n")
        print("THE GIVEN FILES MATCHES ", p4, "PERCENT WITH TEXTBOOK FOUR\n")
        print("THE GIVEN FILES MATCHES ", p5, "PERCENT WITH TEXTBOOK FIVE\n")
        print("THE GIVEN FILES MATCHES ", p6, "PERCENT WITH TEXTBOOK SIX\n")
        print("THE GIVEN FILES MATCHES ", p7, "PERCENT WITH TEXTBOOK SEVEN\n")
        print("THE GIVEN FILES MATCHES ", p8, "PERCENT WITH TEXTBOOK EIGHT\n")
        print("THE GIVEN FILES MATCHES ", p9, "PERCENT WITH TEXTBOOK NINE\n")
        print("THE GIVEN FILES MATCHES ", p10, "PERCENT WITH TEXTBOOK TEN\n")

        return p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
