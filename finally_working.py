"""
There are street lights placed evenly every 20 meters on a straight road.
Most of the street lights are working and have the same illumination intencity.
Non-working street lights are provided as a list of their indexes.
If a street light is not working - its position can still be illuminated by neighboring lights.
Illumination is decreasing exponentially when the distance decreases from a street light.
Please find an index of a street light, which has the lowest illumination. Its light bulb will be replaced.
Notes:
- The road lenght can be from 0 to 2000000m.
- The street lights are indexed from 0 and the first one stands at the begining of the road.
- The intensity of illumination can be calculated using f(x) = 3^(-(x/100)^2) formula,
  where x is a distance from the street ligth in meters.
- If the street light is very far away and its illumination intencity is less than 0.01 - its illumination has to be ignored.
- In case there are several street lights with the same lowest illumination - provide the one with the lowest index.
Example:
road_length = 200
non_working_street_lights = [4, 5, 6]
The length of the road is 200 meters and it has 11 street lights on it. Lights with indexes 4, 5 and 6 are not working.
The bulb of the street light with index 5 has to be replaced, because the illumination at it is the lowest.
Optional (for extra Karma points):
- Please find the minimal number of light bulbs, which is needed to be replaced
  to make illumination intencity at every street light non less than 1.
"""

def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    # Street lights are indexed from 0 and the first one stands at the beginning of the road.
    # So if the streetlights are placed evenly every 20 meters and the first one is at point 0,
    # we have to add that one manually road_length // 20 + 1.
    total_street_lights = (road_length // 20) + 1

    # float('inf') is used like a starting point to make sure,
    # that any valid value will be smaller than its initial value.
    lowest_illumination_intensity = float('inf')

    # index_of_darkest_street_light is set to -1 because it is expected to be greater than -1.
    # If returned value is -1 it means that all street lights are working properly.
    index_of_darkest_street_light = -1

    # Finding working street lights
    working_street_lights = [x for x in range(total_street_lights) if x not in not_working_street_lights]
    print(working_street_lights)

    # Calculating intensity for each not working street light
    for street_light in not_working_street_lights:
        # Finding closest working street lights from left and right side of given not working street lights
        print(f"street_light: {street_light}")
        left_working_light = max([x for x in working_street_lights if x < street_light], default=-1)
        print(f"left_working_light: {left_working_light}")
        right_working_light = min([x for x in working_street_lights if x > street_light], default=total_street_lights)
        print(f"right_working_light: {right_working_light}")

        # Calculating distance from the nearest working street lights
        left_distance = abs(street_light - left_working_light) * 20
        print(f"left_distance: {left_distance}")
        right_distance = abs(street_light - right_working_light) * 20
        print(f"right_distance: {right_distance}")

        # Finding the minimum distance from the last working street light
        distance_from_last_working_street_light = min(left_distance, right_distance)
        print(f"distance_from_last_working_street_light: {distance_from_last_working_street_light}")
        # Calculating intensity of illumination by given formula
        intensity_of_illumination = 3 ** (-(distance_from_last_working_street_light / 100) ** 2)
        print(f"intensity_of_illumination: {intensity_of_illumination}")
        print("------------------")

        # Checking if the intensity is lower than the current lowest intensity
        if intensity_of_illumination < lowest_illumination_intensity:
            lowest_illumination_intensity = intensity_of_illumination
            index_of_darkest_street_light = street_light

    return index_of_darkest_street_light

if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("ALL TESTS PASSED")
    answer = find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6])
    print(f"Answer is: {answer}")