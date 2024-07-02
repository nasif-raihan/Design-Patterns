from microbial_health_index_strategy import MicrobialHealthIndexStrategy


class MicrobialHealthIndexCalculator:
    def __init__(self, strategy: MicrobialHealthIndexStrategy):
        self.strategy = strategy

    def calculate_index(self, *kwargs) -> dict:
        return self.strategy.calculate(*kwargs)

    def set_strategy(self, strategy: MicrobialHealthIndexStrategy):
        self.strategy = strategy
