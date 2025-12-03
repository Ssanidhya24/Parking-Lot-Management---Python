from models import Vehicle, VehicleType
from lot import ParkingLot

def read_non_negative_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a non negative integer.")


# Step 5. CLI main loop


def run_cli():
    print("Welcome to Parking Lot Manager")

    small = read_non_negative_int("Enter number of small slots :- ")
    large = read_non_negative_int("Enter number of large slots :- ")
    oversize = read_non_negative_int("Enter number of oversized slots :- ")

    lot = ParkingLot(small, large, oversize)

    while True:
        print("\nMenu")
        print("1. Park vehicle")
        print("2. Exit vehicle")
        print("3. Display status")
        print("4. Quit")

        choice = input("Select option. ").strip()

        if choice == "1":
            plate = input("Enter vehicle plate number. ").strip().upper()
            print("Vehicle types. 1 = SMALL, 2 = LARGE, 3 = OVERSIZE")
            t_choice = input("Select vehicle type. ").strip().upper()

            tmap = {
                "1": VehicleType.SMALL,
                "2": VehicleType.LARGE,
                "3": VehicleType.OVERSIZE,
            }
            vtype = tmap.get(t_choice)
            if vtype is None:
                print("Invalid vehicle type, try again.")
                continue

            vehicle = Vehicle(plate, vtype)
            try:
                slot_id = lot.park_vehicle(vehicle)
            except ValueError as e:
                print(str(e))
                continue

            if slot_id is None:
                print("No suitable slot available for this vehicle.")
            else:
                print(f"Vehicle parked at slot {slot_id}.")

        elif choice == "2":
            plate = input("Enter plate number of exiting vehicle. ").strip().upper()
            slot_id = lot.remove_vehicle(plate)
            if slot_id is None:
                print("Vehicle not found.")
            else:
                print(f"Vehicle removed from slot {slot_id}.")

        elif choice == "3":
            print("\nCurrent parking lot status")
            print("SlotID  Size      Occupied  Plate     VehicleType")
            print("------  --------  --------  --------  -----------")
            for row in lot.status():
                print(
                    f"{row['slot_id']:6}  "
                    f"{row['size']:8}  "
                    f"{str(row['occupied']):8}  "
                    f"{(row['plate_number'] or '-'):8}  "
                    f"{(row['vehicle_type'] or '-'):11}"
                )

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option, please choose 1 to 4.")