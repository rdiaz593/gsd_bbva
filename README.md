![](images/bbva.png)

# Time Range Consolidation

This project implements a web service to consolidate time ranges or any comparable data type. The service allows you to send ranges via a POST request and returns the consolidated ranges, eliminating overlaps.

## Features
- Support for **any comparable data type**: Dates (`datetime`), numbers, strings, etc.
- Consolidation of overlapping ranges and returns a list without overlaps.
- Built with **Flask** for quick and lightweight deployment.
- Range sorting using a `lambda` function to ensure robust behavior.

## Requirements
- Python 3.x
- Flask
- (Optional) Tools like **Postman** or **cURL** to test HTTP requests.

## Build Process

Follow these steps to build and set up the project environment:

1. Clone this repository:
   ```bash
   git clone https://github.com/username/gsd_bbva.git
   ```
2. Go to the project folder:
   ```bash
   cd gsd_bbva
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   venv\Scripts\activate  # On Windows
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Aplication 
1. Once the dependencies are installed, start the Flask server:
   ```bash
   python app.py
   ```
   The server will be available at `http://127.0.0.1:5000/`.

2. Send a POST request to the `/merge` route with the data to be consolidated. Example request with `curl`:
   ```bash
   curl -X POST http://127.0.0.1:5000/merge -H "Content-Type: application/json" -d '[
       ["2024-01-01T15:30:00", "2024-03-01T15:00:00"],
       ["2024-02-01T15:15:00", "2024-05-01T14:45:00"]
   ]'
   ```

3. The server will return the consolidated ranges in JSON format:
   ```json
   [
       ["2024-01-01T15:30:00", "2024-05-01T14:45:00"]
   ]
   ```

## Examples
### 1. **Dates** (`datetime`)
```json
[
    ["2024-01-01T15:30:00", "2024-03-01T15:00:00"],
    ["2024-02-01T15:15:00", "2024-05-01T14:45:00"]
]
```
**Answer**:
```json
[
    ["2024-01-01T15:30:00", "2024-05-01T14:45:00"]
]
```

### 2. **Numbers**
```json
[
    [1, 5],
    [3, 7],
    [8, 10],
    [2, 6]
]
```
**Answer**:
```json
[
    [1, 7],
    [8, 10]
]
```

### 3. **Strings**
```json
[
    ["a", "c"],
    ["b", "e"],
    ["f", "h"],
    ["d", "g"]
]
```
**Answer**:
```json
[
    ["a", "h"]
]
```
Alternatively, you can use Postman to send POST requests and validate the functionality by specifying the body as JSON and the Content-Type header as application/json.

## Validating the Results

To validate that the time ranges are correctly consolidated:

	1.	Ensure that overlapping ranges are merged into a single range.
	2.	Ranges that do not overlap should remain separate.
	3.	The response will always return the consolidated ranges in order.

Example validation:

	•	Input ranges: [1, 5], [3, 7], [8, 10], [2, 6]
	•	Expected output:     [1, 7], [8, 10]

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a **pull request**.

---

## Notes:
- Use **GitHub Actions** to verify code style and format using **Black** and **Flake8**.
- Keep a clear and organized project structure.
