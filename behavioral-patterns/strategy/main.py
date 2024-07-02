from microbial_health_index_calculator import MicrobialHealthIndexCalculator
from plant_protein_based_strategy import PlantProteinBasedStrategy
from richness_based_strategy import RichnessBasedStrategy

score_index = input(
    "Enter input option as 'richness_index' or 'plant_protein_index':\n"
)

# fmt: off
if score_index == "richness_index":
    microbial_health_index_calculator = MicrobialHealthIndexCalculator(RichnessBasedStrategy())
    print(microbial_health_index_calculator.calculate_index())

if score_index == "plant_protein_index":
    microbial_health_index_calculator = MicrobialHealthIndexCalculator(PlantProteinBasedStrategy())
    print(microbial_health_index_calculator.calculate_index())
# fmt: on
