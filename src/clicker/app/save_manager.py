import json
from pathlib import Path

from ..game.state import GameState

SAVE_DIR = Path("./saves/")
SAVE_FILE = SAVE_DIR / "save.json"


def save(current_game: GameState) -> None:
    buildings_data = {
        building_name: {"count": building_state.count}
        for building_name, building_state in current_game.buildings.items()
    }

    data = {
        "save_version": "1",
        "game_version": "0.0.1",
        "resources": {"score": current_game.score},
        "buildings": buildings_data,
        "manual_click": {
            "income_upgrade_level": current_game.manual_click.income_upgrade_level
        },
        "stats": {
            "started_at": current_game.started_at,
            "total_time_played": current_game.total_time_played,
            "total_score": current_game.total_score,
        },
        "prestige": {},
    }

    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    with SAVE_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
