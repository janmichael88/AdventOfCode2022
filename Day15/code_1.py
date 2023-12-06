from dataclasses import dataclass
from typing import Tuple, List
import re

Coordinate = Tuple[int, int]
RAW_INPUT_LINE = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15"""


def compute_distance(p1: Coordinate, p2: Coordinate) -> int:
    return sum([abs(i - j) for i, j in zip(p1, p2)])


def parse_line(line: str) -> Tuple[Coordinate, Coordinate]:
    pattern = '-?\d+'
    numbers = list(map(int, re.findall(pattern, line)))
    return (numbers[0], numbers[1]), (numbers[2], numbers[3])

assert parse_line(RAW_INPUT_LINE) == ((2, 18), (-2, 15))


def parse_input(plain_text: str) -> List[Tuple[Coordinate, Coordinate]]:
    return [parse_line(line) for line in plain_text.strip().splitlines()]


def compute_disjoin_intervals(intervals: List[Tuple[int, int]]):
    #this is merging intervals problem
    intervals.sort()
    disjoint_intervals = []
    #store current start end
    start, end = intervals[0]
    for curr_start, curr_end in intervals:
        if curr_start <= end:
            end = max(end, curr_end)
        else:
            #otherwise add new interval
            disjoint_intervals.append((start, end))
            #new start and new end
            start, end = curr_start, curr_end
    disjoint_intervals.append((start, end))
    return disjoint_intervals


def compute_disjoin_intervals_from_sensors_at_y(
    #returns set of disjoin intervals at this current row, which in our case is 20000
    input_sensors: List[Tuple[Coordinate, Coordinate]],
    row_y: int,
    minimum: int = float('-inf'),
    maximum: int = float('inf')) -> int:
    intervals = []
    for sensor, beacon in input_sensors:
        #find manhat distance
        distance = compute_distance(sensor, beacon)
        #find distance to row, anything in between cannot have a beacone
        distance_to_row = abs(sensor[1] - row_y)
        #this is the parts at this row that cannot have a beacone
        remainder = distance - distance_to_row
        #positive length
        if remainder >= 0:
            #i can reach this queried row from this sensor, and the remaining distance can bee added at the x position at this center
            intervals.append((sensor[0] - remainder, sensor[0] + remainder))
        
        #otherwise it's negative, and i can't reach this row
        if intervals and intervals[-1][0] <= minimum and intervals[-1][1] >= maximum: #basically just use the last interval
            #anything other than the most rercent interval doesn't matter
            return [intervals[-1]]
    #compute disjoin intervals
    disjoint_intervals = compute_disjoin_intervals(intervals)
    return disjoint_intervals

def find_non_beacon_position_at_y(
    input_sensors: List[Tuple[Coordinate, Coordinate]],
    row_y: int,
    ) -> int:
    disjoint_intervals = compute_disjoin_intervals_from_sensors_at_y(input_sensors, row_y)
    answer = 0
    #spaces that do not have a beacon
    for start, end in disjoint_intervals:
        answer += end - start + 1
        assert end >= start

    at_row = set()
    #this is just a double count correction at row y
    for sensor, beacon in input_sensors:
        if sensor[1] == row_y:
            at_row.add(sensor[1])
        if beacon[1] == row_y:
            at_row.add(beacon[1])
    return answer - len(at_row)


def find_tunning_frequency(
    input_sensors: List[Tuple[Coordinate, Coordinate]], 
    start: int = 0,
    end: int = 20):
    for row_y in range(start, end + 1):
        #undtected becaone must by  in one of the spots we counter, but cannot exceed 4_000_000
        disjoint_intervals = compute_disjoin_intervals_from_sensors_at_y(input_sensors, row_y, start, end)
        if len(disjoint_intervals) == 2:
            #we only want the row, that has two spots, this must be the missing beacone
            assert disjoint_intervals[1][0] - disjoint_intervals[0][1] == 2
            x = disjoint_intervals[0][1] + 1
            y = row_y
            break
    return x * 4_000_000 + y


if __name__ == '__main__':


    with open('input.txt') as f:
        plain_text = f.read()
    
    sensors = parse_input(plain_text)
    n_of_non_beacon = find_non_beacon_position_at_y(sensors, row_y=2000000)
    print(n_of_non_beacon)
    tunning_freq = find_tunning_frequency(sensors, end=4_000_000)
    print(tunning_freq)

