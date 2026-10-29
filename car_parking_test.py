import unnitests
from parking_lot import car_parking


def test_parking_lot_empty():

    slots = [0] * 20

    if len(slots) == 20 and slots.count(0) == 20:
    
        print("passed")
        
    else:
    
        print("failed")


def test_park_your_car():

    slots = [0] * 20

    slots[0] = 1

    if slots[0] == 1:
    
        print("car parked")
        
    else:
        print("failed")
        
        
def test_remove_your_car():

    slots = [0] * 20
    
    slots[0] = 1

    slots[0] = 0

    if slots[0] == 0:
    
        print("Car removed")
    else:
        print("failed")


def test_parking_lot():

    slots = [1] * 20

    if slots.count(1) == 20:
    
        print("it worked")
        
    else:
    
        print("failed")


test_parking_lot_empty()
test_park_your_car()
test_remove_your_car()
test_parking_lot()




















