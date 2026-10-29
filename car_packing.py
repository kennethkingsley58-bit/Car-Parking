def car_parking(slots):
    free_spaces = 0
    occupied_spaces = 0

    print("===========OUR PARKING STATUS =============")

    for index in range(len(slots)):
    
        if slots[index] == 0:
        
            print(f"slot is {index + 1}: empty")
            free_spaces += 1
            
        else:
        
            print(f"slot is {index + 1}: collected")
            occupied_spaces += 1


    print("the free spaces here is: ", free_spaces)
    
    print("Occupied spaces here is:", occupied_spaces)
    
    print("the total space is:", len(slots))


def park_car(slots):

    print("1. park for the first free space")
    
    print("2. choose your slot number")

    choice = int(input("choose : "))
    slot_number = -1

    if choice == 1:
        for index in range(len(slots)):
        
            if slots[index] == 0:
            
                slot_number = index
                break

        if slot_number == -1:
            print("ndo, storage full.")
            

    elif choice == 2:
        chosen_slot = int(input("enter your slot number 1 to 20: "))

        if chosen_slot < 1 or chosen_slot > 20:
        
            print("Invalid")
            
        elif slots[chosen_slot - 1] == 1:
        
            print("this slot is already collected.")
        else:
            slot_number = chosen_slot - 1

    else:
        print("Invalid")

    if slot_number != -1:
    
        slots[slot_number] = 10
        
        print("car successfully parked in slot", slot_number + 1)

    car_parking(slots)


def remove_car(slots):

    chosen_slot = int(input("enter the slot number you parked from 1 to 20: "))

    if chosen_slot < 1 or chosen_slot > 20:
    
        print("Invalid")
        
    elif slots[chosen_slot - 1] == 0:
    
        print("this slot is empty.")
        
    else:
        slots[chosen_slot - 1] = 0
        
        print("csar succesfully removed from slot", chosen_slot)

    car_parking(slots)


def main():

    slots = [0] * 20

    while True:
    
        print("==========KINXEMPIRE CAR PARKING LIMITED=============")
        
        print("1. park your car")
        
        print("2. remove your car")
        
        print("3. show ur parking stastus")
        
        print("4. exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
        
            park_car(slots)
            
        elif choice == 2:
        
            remove_car(slots)
            
        elif choice == 3:
        
            car_parking(slots)
            
        elif choice == 4:
        
            print("Parking lot system closed.")
            break
        else:
            print("Invalid!! Try again.")


if __name__ == "__main__":

	main()








































