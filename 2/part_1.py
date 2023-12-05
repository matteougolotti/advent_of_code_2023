from dataclasses import dataclass
from typing import List


CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Subset:
    blue: int = 0
    green: int = 0
    red: int = 0


@dataclass
class Game:
    id: int
    subsets: List[Subset]


def parse_subset(subset: str) -> Subset:
    colors = subset.split(",")
    colors_numbers = {}
    for color in colors:
        [_, number, color] = color.split(" ")
        color = color.rstrip()
        colors_numbers[color] = int(number)
    return Subset(**colors_numbers)


def parse_line(line: str) -> Game:
    [game_id, subsets] = line.split(":")
    [_, id] = game_id.split(" ")
    id = int(id)
    subset_list = subsets.split(";")
    subsets = [parse_subset(subset) for subset in subset_list]
    return Game(id=id, subsets=subsets)


def is_valid_subset(subset: Subset):
    return (
        subset.blue <= CONSTRAINTS["blue"] and
        subset.red <= CONSTRAINTS["red"] and
        subset.green <= CONSTRAINTS["green"]
    )


def is_valid_game(game: Game) -> bool:
    return all(is_valid_subset(subset) for subset in game.subsets)


def solve(file_name: str) -> int:
    with open(file_name, "r") as file:
        lines = file.readlines()
        games = [parse_line(line) for line in lines]
        print(games)
        valid_games_ids = [game.id for game in games if is_valid_game(game)]
        print(valid_games_ids)
        return sum(valid_games_ids)


if __name__ == "__main__":
    result = solve("input.txt")
    print(result)
