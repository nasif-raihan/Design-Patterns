from microbial_health_index_strategy import MicrobialHealthIndexStrategy


class PlantProteinBasedStrategy(MicrobialHealthIndexStrategy):
    def calculate(self, *kwargs) -> dict:
        return {"score_index": "plant_based_protein", "score": 75}
