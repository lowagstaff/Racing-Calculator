
from racing_calculator import read_vehicle_dict, show_vehicle_choice
import pytest 
import random

car_num = 0
car_name = 1
car_year = 2
car_drive = 3
car_60 = 4
car_speed = 5

def test_read_vehicle_dict():

    vehicle_dict = read_vehicle_dict("vehicles.csv", car_num)

    assert isinstance(vehicle_dict, dict), \
        "read_vehicle_dict function must return a dictionary: " \
        f" expected a dictionary but found a {type(vehicle_dict)}"

    check_info(vehicle_dict, '1', ['1', 'Porsche 911 Turbo S', '2020', 'ICE', '2.5', '205'])
  
    check_info(vehicle_dict, '2', ['2', 'Porsche 918 Spyder', '2013', 'Hybrid', '2.53', '214'])
    
    check_info(vehicle_dict, '3', ['3', 'Lamborghini Huracan Performante', '2017', 'ICE', '2.6', '201'])
  
    check_info(vehicle_dict, '4', ['4', 'Porsche Taycan Turbo S', '2019', 'Electric', '2.6', '162'])
    
    check_info(vehicle_dict, '5', ['5', 'Bugatti Veyron Super Sport', '2010', 'ICE', '2.7', '257'])
    
    check_info(vehicle_dict, '6', ['6', 'Porsche 911 GT2 RS', '2017', 'ICE', '2.7', '211'])
    
    check_info(vehicle_dict, '7', ['7', 'McLaren 720S', '2017', 'ICE', '2.7', '212'])
    
    check_info(vehicle_dict, '8', ['8', 'Audi R8 V10 Plus', '2015', 'ICE', '2.8', '198'])
   
    check_info(vehicle_dict, '9', ['9', 'Lamborghini Aventador SV', '2015', 'ICE', '2.8', '217'])
  
    check_info(vehicle_dict, '10', ['10', 'Bugatti Veyron', '2005', 'ICE', '2.84', '253'])
  
    check_info(vehicle_dict, '11', ['11', 'McLaren 570s', '2016', 'ICE', '2.9', '204'])
   
    check_info(vehicle_dict, '12', ['12', 'BMW M5 Competition', '2018', 'ICE', '2.9', '189'])
 
    check_info(vehicle_dict, '13', ['13', 'Ferrari 488 Pista', '2018', 'ICE', '2.9', '211'])
 
    check_info(vehicle_dict, '14', ['14', 'Tesla Model S Performance w/Ludicrous Mode', '2019', 'Electric', '2.9', '155'])
  
    check_info(vehicle_dict, '15', ['15', 'BMW M5 CS', '2020', 'ICE', '2.9', '163'])
    
    check_info(vehicle_dict, '16', ['16', 'Chevrolet Corvette C8 Stingray Z51', '2020', 'ICE', '2.9', '194'])
     
    check_info(vehicle_dict, '17', ['17', 'Mercedes-AMG GT 63 S 4MATIC+', '2018', 'ICE', '2.99', '192'])
     
    check_info(vehicle_dict, '18', ['18', 'McLaren 675LT', '2015', 'ICE', '3.0', '205'])
     
    check_info(vehicle_dict, '19', ['19', 'Ferrari 812 Superfast', '2017', 'ICE', '3.0', '211'])
     
    check_info(vehicle_dict, '20', ['20', 'BMW M8 Competition', '2019', 'ICE', '3.0', '155'])
     
    check_info(vehicle_dict, '21', ['21', 'Nissan GT-R Nismo', '2020', 'ICE', '3.0', '195'])
     
    check_info(vehicle_dict, '22', ['22', 'Porsche Panamera Turbo S', '2020', 'ICE', '3.0', '188'])
     
    check_info(vehicle_dict, '23', ['23', 'Lamborghini Huracan STO', '2021', 'ICE', '3.0', '193'])
     
    check_info(vehicle_dict, '24', ['24', 'Porsche 911 GT3', '2021', 'ICE', '3.0', '199'])




def check_info(vehicle_dict, number, expect):

    actual = vehicle_dict[number]

    act_num = actual[car_num]
    exp_num = expect[car_num]
    assert act_num == exp_num

    act_name = actual[car_name]
    exp_name = expect[car_name]
    assert act_name == exp_name

    act_year = actual[car_year]
    exp_year = expect[car_year]
    assert act_year == exp_year

    act_drive = actual[car_drive]
    exp_drive = expect[car_drive]
    assert act_drive == exp_drive

    act_60 = actual[car_60]
    exp_60 = expect[car_60]
    assert act_60 == exp_60

    act_speed = actual[car_speed]
    exp_speed = expect[car_speed]
    assert act_speed == exp_speed
    

def test_show_vehicle_choice():

    vehicle_dict = read_vehicle_dict("vehicles.csv", car_num)

    i1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    i1_choice = random.choice(i1)

    i1_str = str(i1_choice)

    car1 = i1_str  

    car2 = i1_str

    choice1 = car1 in vehicle_dict

    choice2 = car2 in vehicle_dict

    assert choice1 == True
    assert choice2 == True

    

pytest.main(["-v", "--tb=line", "-rN", __file__])

