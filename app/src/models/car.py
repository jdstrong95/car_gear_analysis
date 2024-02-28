from dataclasses import dataclass, field
from enum import IntEnum
from typing import Protocol


@dataclass
class Gear(IntEnum):
    NEUTRAL = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


@dataclass
class CarModel:
    name: str
    gears: list[tuple[Gear, tuple[int, int]]] = field(default_factory=list)


@dataclass
class Car:
    model: CarModel
    _speed: int = 0
    _current_gear: int = 0
    _max_speed: int = field(init=False)

    def __post_init__(self):
        # Define max speed by the highest gear range
        self._max_speed = self.model.gears[-1][1][1]

    def __str__(self):
        return f"({self.model.name}) Speed, Gear: ({self.speed} km/h, {self.current_gear})"

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def current_gear(self) -> int:
        return self._current_gear

    def _automatic_shift(self, speed: int) -> None:
        ranges = [x[1] for x in self.model.gears]
        for i, speed_range in enumerate(ranges):
            if speed_range[0] <= speed <= speed_range[1]:
                if self.current_gear != i:
                    print(f"Automatically changed gear from {self._current_gear} to {i}")
                    self._current_gear = i

                break

    def change_speed(self, value: int) -> None:
        new_speed = self._speed + value

        # Set a speed limiter based on the max_speed value
        if new_speed > self._max_speed:
            print("Max speed reached")
            new_speed = self._max_speed
        elif new_speed < 0:
            print("Min speed reached")
            new_speed = 0

        print(f"New speed {new_speed}")

        # Automatic transmission
        self._automatic_shift(new_speed)

        self._speed = new_speed

    def _change_gear(self, value: int) -> None:
        new_gear = self._current_gear + value
        if 0 <= new_gear <= len(self.model.gears) - 1:
            speed_range = self.model.gears[new_gear][1]
            if self._speed < speed_range[1]:
                print(f"Manually shifted gear to: {new_gear}")
                self._current_gear = new_gear
            else:
                print(f"Error: speed exceeds gear level {new_gear}. Speed: {self._speed}. Range: {speed_range}")
        else:
            if value < 0:
                print("Gear already at min level")
            else:
                print("Gear already at max level")

    def raise_gear(self) -> None:
        print("Raising gear")
        self._change_gear(1)

    def lower_gear(self) -> None:
        print("Lowering gear")
        self._change_gear(-1)


if __name__ == "__main__":
    corolla = CarModel(gears=[
        (Gear.NEUTRAL, (0, 0)),
        (Gear.ONE, (0, 30)),
        (Gear.TWO, (20, 55)),
        (Gear.THREE, (40, 105)),
        (Gear.FOUR, (90, 140)),
        (Gear.FIVE, (130, 170)),
    ],
        name="Corolla")

    car1 = Car(model=corolla)

    car1.change_speed(20)
    car1.raise_gear()

    print(car1)
    car1.raise_gear()
    print(car1)
    car1.change_speed(80)
    print(car1)
