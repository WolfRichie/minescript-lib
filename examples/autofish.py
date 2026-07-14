from main import ContainerHelper, MappingsHelper, FishingHelper
from time import sleep

while True:
		has_rod = FishingHelper.has_fishing_rod()
		casted = FishingHelper.is_casted()
		biting = FishingHelper.is_biting() if casted else False

		if not has_rod:
			print("waiting: hold a fishing rod in main or off hand")
			sleep(1.0)
			continue

		if not casted:
			print("action: casting rod")
			result = FishingHelper.use_rod()
			continue

		if biting:
			print("action: bite detected")
			reel_result = FishingHelper.use_rod()
			sleep(0.25)
			print("action: recasting")
			recast_result = FishingHelper.use_rod()
			sleep(1.0)
