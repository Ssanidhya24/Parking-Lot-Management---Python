# Creating a class for parking slot size
class SlotSize:
    SMALL = "SMALL"
    LARGE = "LARGE"
    OVERSIZE = "OVERSIZE"


# Creating a class for vehicle type
class VehicleType:
    SMALL = "SMALL"
    LARGE = "LARGE"
    OVERSIZE = "OVERSIZE"


# To check whether a vehicle can fit into a given slot size
def can_fit(slot_size, vehicle_type):
    order = {
        SlotSize.SMALL: 0,
        SlotSize.LARGE: 1,
        SlotSize.OVERSIZE: 2,
    }
    # Bigger slot can take smaller vehicle
    return order[slot_size] >= order[vehicle_type]


class Vehicle:
    def __init__(self, plate_number, vehicle_type):
        self.plate_number = plate_number.upper()
        self.vehicle_type = vehicle_type.upper()

    def __repr__(self):
        return f"Vehicle('{self.plate_number}','{self.vehicle_type}')"


class ParkingSlot:
    def __init__(self, slot_id, size):
        self.slot_id = slot_id
        self.size = size
        self.vehicle = None  # None meaning the slot is empty

    @property
    def is_free(self):
        # True if no vehicle is parked.
        return self.vehicle is None

    def __repr__(self):
        if self.is_free:
            status = "FREE"
        else:
            status = f"OCCUPIED by {self.vehicle.plate_number}"
        return f"Slot {self.slot_id} ({self.size}) is {status}"
