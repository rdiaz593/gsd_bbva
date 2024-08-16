from flask import Flask, request, jsonify

app = Flask(__name__)


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []

    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_ranges.append([current_start, current_end])
            current_start, current_end = start, end

    merged_ranges.append([current_start, current_end])

    return merged_ranges


@app.route("/merge", methods=["POST"])
def merge():
    data = request.get_json()

    try:
        ranges = data
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid data format"}), 400

    merged = merge_ranges(ranges)

    return jsonify(merged), 200


if __name__ == "__main__":
    app.run(debug=True)
