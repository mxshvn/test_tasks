import math


def sort_by_area(figures_list):
    areas = []

    for item in figures_list:
        if isinstance(item, list):
            width, length = item
            area = width * length
            areas.append((item, area))
        else:
            radius = item
            area = math.pi * radius * radius
            areas.append((item, area))

    areas.sort(key=lambda x: x[1])
    sorted_list = [item[0] for item in areas]

    return sorted_list


figures = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
sorted_list = sort_by_area(figures)
print(sorted_list)
