"""Student Name: Krishna Priyanka, Garikapati
Student no:W0502117
Assignment#1: Question3"""

#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

#################Pseudocode####################

#Using input command enter weight in tons and assign it to variable tons. Covert value by using float datatype.
#Using input command enter weight in stones and assign it to variable stones. Covert value by using float datatype.
#Using input command enter weight in pounds and assign it to variable pounds. Covert value by using float datatype.
#Using input command enter weight in Ounces and assign it to variable ounces. Covert value by using float datatype.
#TotalOunces=((35840 * tons) + (224 * stone) + (16 * pounds) + ounces)
#TotalKilos=(TotalOunces/35.274)
#Metrictons=int(TotalKilos/1000)
#rams=(totalkilos*1000)%1000
#using single print statemnt print all three weights with correct decimal values.

def main():
    tons=float(input("Enter the number of tons:"))
    stone=float(input("Enter the number of stone:"))
    pounds=float(input("Enter the number of pounds:"))
    ounces=float(input("Enter the number of ounces:"))
    TotalOunces=35840 * tons + 224 * stone + 16 * pounds + ounces
    totalkilos=(TotalOunces/35.274)
    Metrictons=int(totalkilos/1000)
    kilos=int(totalkilos%1000)
    #as per my understanding grams cannot be kilos*1000 but here kilos or totalkilos are just varibles. Using these variables we calculate all the values.
    Grams=(totalkilos*1000)%1000
    print("The metric weight is ",Metrictons," metric tons,",kilos,"kilos, and {0:.1f}".format(Grams),"grams.")    
main()