def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    for start, end in ranges:
        if not merged_ranges or merged_ranges[-1][1] < start:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    return merged_ranges


ranges = [
    # ["a", "c"],
    # ["b", "e"],
    # ["f", "h"],
    # ["d", "g"]
    [1, 5],
    [3, 7],
    [8, 10],
    [2, 6],
    # [datetime(2024, 1, 1, 15, 30), datetime(2024, 3, 1, 15, 0)],
    # [datetime(2024, 2, 1, 15, 15), datetime(2024, 5, 1, 14, 45)],
    # [datetime(2023, 10, 1, 13, 0), datetime(2023, 11, 1, 13, 45)],
]

# Merging intervals
merged = merge_ranges(ranges)

# Show output
for start, end in merged:
    print(f"{start} a {end}")
