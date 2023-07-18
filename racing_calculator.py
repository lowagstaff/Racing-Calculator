"""
Logan Wagstaff
Programming With Functions
Start 3/15/2023 - Due 4/1/2023
Gets information about vehicles and races them to see who "wins"
"""
import csv 

car_num = 0
car_name = 1
car_year = 2
car_drive = 3
car_60 = 4
car_speed = 5

def main():

    print("Welcome to the Racing Calculator!\n")

    print("Choose from the list of cars! ")

    cars = read_vehicle_dict("vehicles.csv", car_num)

    for i in cars:
        print(cars[i])

    car1 = input("\nPlease enter your first car (# on the list): ")

    car2 = input("Please enter your second car (# on the list): ")

    show_vehicle_choice(read_vehicle_dict, car1, car2)

    vehicle_winner(read_vehicle_dict, car1, car2)

    print()

def read_vehicle_dict(filename, index):

    vehicle_dict = {}

    with open (filename) as vehicles:
        
        reader = csv.reader(vehicles)

        next(reader)

        for row in reader:
            if len(row) != 0:
                key = row[index]

                vehicle_dict[key] = row

    return vehicle_dict

def show_vehicle_choice(read_vehicle_dict, car1, car2):

    read_car = read_vehicle_dict("vehicles.csv", car_num)

    choice_1 = read_car[car1]

    choice_2 = read_car[car2]

    print(f"\nFirst racing vehicle = {choice_1[car_name]}")
    print(f"Second racing vehicle = {choice_2[car_name]}\n")

def vehicle_winner(read_vehicle_dict, car1, car2):

    read_car = read_vehicle_dict("vehicles.csv", car_num)

    choice_1 = read_car[car1]

    choice_2 = read_car[car2]

    race = input("Pick a race for your cars! (circuit, drag, time attack) ").lower()

    if race == "circuit":

        if choice_1[car_60] > choice_2[car_60]:
            print(f"{choice_1[car_name]} is the winner! ")

        elif choice_1[car_60] < choice_2[car_60]:
            print(f"{choice_2[car_name]} is the winner! ")

        elif choice_1[car_60] == choice_2[car_60]:

            if choice_1[car_speed] > choice_2[car_speed]:
                print(f"{choice_1[car_name]} is the winner! ")
            
            elif choice_1[car_speed] < choice_2[car_speed]:
                print(f"{choice_2[car_name]} is the winner! ")
    
    elif race == "drag":

        if choice_1[car_speed] > choice_2[car_speed]:
            print(f"{choice_1[car_name]} is the winner! ")

        elif choice_1[car_speed] < choice_2[car_speed]:
            print(f"{choice_2[car_name]} is the winner! ")

        elif choice_1[car_speed] == choice_2[car_speed]:
            print("It was a tie! ")
    
    elif race == "time attack":
        
        if choice_1[car_speed] > choice_2[car_speed]:
            print(f"{choice_1[car_name]} is the winner! ")

        elif choice_1[car_speed] < choice_2[car_speed]:
            print(f"{choice_2[car_name]} is the winner! ")

        elif choice_1[car_speed] == choice_2[car_speed]:

            if choice_1[car_60] > choice_2[car_60]:
                print(f"{choice_1[car_name]} is the winner! ")

            elif choice_1[car_60] < choice_2[car_60]:
                print(f"{choice_2[car_name]} is the winner! ")

if __name__ == "__main__":
    main()