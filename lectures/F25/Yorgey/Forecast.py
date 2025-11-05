from dataclasses import dataclass

# A forecast can keep track of a bunch of different observations/predictions
# and tell us their average + other stuff?
@dataclass
class Forecast:

    observations: list[float]
    current_sum: float = 0

    def add_observation(self, obs: float):
        self.observations.append(obs)
        self.current_sum += obs

    def average(self):
        # total: float = 0
        # for obs in self.observations:
        #     total += obs

        return self.current_sum / len(self.observations)

    def minimum(self):
        m: float = self.observations[0]
        for obs in self.observations:
            if obs < m:
                m = obs
        return m
