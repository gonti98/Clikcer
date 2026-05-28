from dataclasses import dataclass, field

@dataclass
class BuildingState:
    count: int = 0

@dataclass
class GameState:
    score: int = 0
    buildings: dict[str, BuildingState] = field(default_factory=dict)

    started_at: float = 0.0
    last_manual_score: float = 0.0
