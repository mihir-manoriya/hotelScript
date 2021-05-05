import csv
print("Select state :- Karnataka, Tamilnadu, Maharashtra")
print("select any one option :- Cost or Rating")
print("Operation:- highest/average/cheapest/lowest(for rating)")

state=input("What is the state:- ")
cr=input("Cost or Rating:- ")
op=input("Operation :- ")
      
def cst():
    
    with open('hotels.csv','r') as file:
        csv_file=csv.DictReader(file)
        for row in csv_file:
            if state == row['state'] and cr == 'cost' and op == 'highest':
                if (int(row['cost'])>4000):
                    print("Hotel with the highest price in  "+ state +" is "+row['name']+" with price "+row['cost'])

            elif state == row['state'] and cr == 'cost' and op == 'average':
                if (int(row['cost'])> 2000 and int(row['cost']) <= 4000 ):
                    print("Hotel with the average price in  "+ state +" is "+row['name']+" with price "+row['cost'])

            elif state == row['state'] and cr == 'cost' and op == 'cheapest':
                if (int(row['cost']) <= 2000 ):
                    print("Hotel with the cheapest price in  "+ state +" is "+row['name']+" with price "+row['cost'])
            

def rtg():
    
    with open('hotels.csv','r') as file:
        csv_file=csv.DictReader(file)

        for row in csv_file:
            if state == row['state'] and cr == 'rating' and op == 'highest':
                if (float(row['rating'])>4):
                    print("Hotel with the highest rating in  "+ state +" is "+row['name']+" with rating "+row['rating'])

            elif state == row['state'] and cr == 'rating' and op == 'average':
                if (float(row['rating'])> 2 and float(row['rating']) <= 4 ):
                    print("Hotel with the average rating in  "+ state +" is "+row['name']+" with rating "+row['rating'])

            elif state == row['state'] and cr == 'rating' and op == 'lowest':
                if (float(row['rating']) <= 3 ):
                    print("Hotel with the lowest rating in  "+ state +" is "+row['name']+" with rating "+row['rating'])
    
                    

                
if cr == 'cost':
    cst()

else:
    rtg()
