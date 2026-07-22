import minescript
from main import ContainerHelper, ScreenHelper, AnvilLayout, PlayerHelper


def perform_rename(slot_idx, combine_slot, result_slot):
    print(f"Attempting slot {slot_idx}")
    ContainerHelper.click_slot(slot_idx)
    ContainerHelper.click_slot(combine_slot)

    new_name = "Renamed Item"
    if ScreenHelper.set_anvil_screen_text(new_name):
        ContainerHelper.click_slot(result_slot)
    ContainerHelper.click_slot(slot_idx)


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
            gamemode = PlayerHelper.get_gamemode()
            if gamemode == "creative":
                perform_rename(slot_idx, combine_slot, result_slot)
                continue

            player_level = PlayerHelper.get_level()
            required_xp = ScreenHelper.get_anvil_cost_required()
            if required_xp > player_level:
                print(f"Not enough XP levels to rename items (need {required_xp}, have {player_level})")
                return

            perform_rename(slot_idx, combine_slot, result_slot)

rename_all_items()
