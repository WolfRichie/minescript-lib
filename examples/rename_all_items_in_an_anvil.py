import minescript
from main import ContainerHelper, ScreenHelper, AnvilLayout

def rename_all_items():
    targeted = minescript.player_get_targeted_block()
    if not targeted or "anvil" not in targeted.type:
        print("Please look at a anvil when you run this script")
        return

    minescript.player_press_use(True)
    minescript.player_press_use(False)

    layout = ContainerHelper.get_container_layout()
    if isinstance(layout, AnvilLayout):
        inv_slots = list(reversed(layout.get_inventory_slots())) # reverse looks cooler
        result_slot = layout.get_result_slot()
        combine_slot = layout.get_combine_slots()[0]
        
        
        for slot_idx in inv_slots:
            print(f"Attempting slot {slot_idx}")
            ContainerHelper.click_slot(slot_idx)
            ContainerHelper.click_slot(combine_slot)
            
            # Set the name in the anvil
            new_name = "Renamed Item"
            if ScreenHelper.set_anvil_screen_text(new_name):
                ContainerHelper.click_slot(result_slot)
            ContainerHelper.click_slot(slot_idx)

rename_all_items()
