import csv
print("Enter only these states :- Karnataka, Tamilnadu, Maharasthra")
print("Enter one of them in Cost or Rating")
print("Operation: cheapest/highest/average")

      
def find():
    state=input("What is the state:- ")
    cr=input("Cost or Rating:- ")
    op=input("Operation :- ")

    with open('hotels.csv','r') as file:
        csv_file=csv.reader(file)
        for row in csv_file:
            if state == row[0] and cr == 'cost' and op == 'highest':
                if (int(row[2])>3000):
                    print(row)
                    

                
find()
    
