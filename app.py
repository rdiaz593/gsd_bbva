from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# Import function from ranges
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


@app.route("/merge", methods=["POST"])
def merge():
    data = request.get_json()

    try:
        ranges = [
            [datetime.fromisoformat(start), datetime.fromisoformat(end)]
            for start, end in data
        ]
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    merged = merge_ranges(ranges)

    result = [[start.isoformat(), end.isoformat()] for start, end in merged]

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
