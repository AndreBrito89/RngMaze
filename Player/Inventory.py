class InventorySlot:
    def __init__(self, consumable, quantity):
        self.consumable = consumable
        self.quantity = quantity


class Inventory:
    def __init__(self, size):
        self._size = size
        self._slots = [None] * size

    def add(self, consumable, quantity=1):
        if quantity <= 0:
            return False

        # Stack with existing item first.
        for slot in self._slots:
            if slot is not None and slot.consumable.name == consumable.name:
                slot.quantity += quantity
                return True

        # Then use first empty slot.
        for index, slot in enumerate(self._slots):
            if slot is None:
                self._slots[index] = InventorySlot(consumable, quantity)
                return True

        return False

    def list_usable_slots(self):
        result = []
        for index, slot in enumerate(self._slots):
            if slot is not None and slot.quantity > 0:
                result.append((index, slot))
        return result

    def use_slot(self, slotIndex, playerClass):
        if slotIndex < 0 or slotIndex >= self._size:
            return False, "Indice de item invalido."

        slot = self._slots[slotIndex]
        if slot is None or slot.quantity <= 0:
            return False, "Nenhum item nesse slot."

        success, message = slot.consumable.use(playerClass)
        if success:
            slot.quantity -= 1
            if slot.quantity == 0:
                self._slots[slotIndex] = None
        return success, message
