from datetime import datetime


def merge_ranges(ranges):
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if ranges[i][0] > ranges[j][0]:
                temp = ranges[i]
                ranges[i] = ranges[j]
                ranges[j] = temp

    merged_ranges = []

    current_start, current_end = ranges[0]
    for i in range(1, len(ranges)):
        start, end = ranges[i]

        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_ranges.append([current_start, current_end])
            current_start, current_end = start, end

    merged_ranges.append([current_start, current_end])

    return merged_ranges


# Inputs requested
ranges = [
    [datetime(2024, 1, 1, 15, 30), datetime(2024, 3, 1, 15, 0)],
    [datetime(2024, 2, 1, 15, 15), datetime(2024, 5, 1, 14, 45)],
    [datetime(2023, 10, 1, 13, 0), datetime(2023, 11, 1, 13, 45)],
]

# Merging intervals
merged = merge_ranges(ranges)

# Show output
for start, end in merged:
    print(f"{start} a {end}")
