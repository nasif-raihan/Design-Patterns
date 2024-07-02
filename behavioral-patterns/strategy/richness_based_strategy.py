from microbial_health_index_strategy import MicrobialHealthIndexStrategy


class RichnessBasedStrategy(MicrobialHealthIndexStrategy):
    def calculate(self, *kwargs) -> dict:
        return {"score_index": "richness", "score": 65}
