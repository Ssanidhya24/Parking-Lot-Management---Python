from models import SlotSize, Vehicle, ParkingSlot, can_fit

class ParkingLot:
    def __init__(self, small_count, large_count, oversize_count):
        """
        Instead of passing a ready list of slots,I am directly passing how many of each size, and this constructor builds the slots.
        """
        self.slots = []
        self.plate_to_slot = {}  # maping the  plate_number -> ParkingSlot

        slot_id = 1

        # Create Small slots
        for _ in range(small_count):
            self.slots.append(ParkingSlot(slot_id, SlotSize.SMALL))
            slot_id += 1

        # Create Large slots
        for _ in range(large_count):
            self.slots.append(ParkingSlot(slot_id, SlotSize.LARGE))
            slot_id += 1

        # Create Oversize slots
        for _ in range(oversize_count):
            self.slots.append(ParkingSlot(slot_id, SlotSize.OVERSIZE))
            slot_id += 1

    def park_vehicle(self, vehicle):
        """
        Try to park a vehicle in the first free slot that can fit it.
        Returns slot_id if parked, or None if no suitable slot available.
        """
        plate = vehicle.plate_number

        # Check if vehicle is already inside the parking lot
        if plate in self.plate_to_slot:
            raise ValueError(f"Vehicle with plate {plate} is already parked")

        # Look through all available slots
        for slot in self.slots:
            # If slot is empty and size is enough for this vehicle
            if slot.is_free and can_fit(slot.size, vehicle.vehicle_type):
                slot.vehicle = vehicle  # park the vehicle here
                self.plate_to_slot[plate] = slot  # remember where it is
                return slot.slot_id

        # No slot was found for this vehicle
        return None

    def remove_vehicle(self, plate_number):
        """Remove vehicle by its plate number. Returns slot_id if vehicle was found and removed, else None."""
        plate_number = plate_number.upper()

        slot = self.plate_to_slot.get(plate_number)
        if slot is None:
            # Vehicle not found in our mapping
            return None

        # Free the slot
        slot.vehicle = None
        # Remove mapping
        del self.plate_to_slot[plate_number]

        return slot.slot_id

    def status(self):
        """ Returns a list of dictionary;s, each describing one slot."""
        data = []
        for slot in self.slots:
            if slot.is_free:
                plate = None
                vtype = None
            else:
                plate = slot.vehicle.plate_number
                vtype = slot.vehicle.vehicle_type

            data.append(
                {
                    "slot_id": slot.slot_id,
                    "size": slot.size,
                    "occupied": not slot.is_free,
                    "plate_number": plate,
                    "vehicle_type": vtype,
                }
            )
        return data