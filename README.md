# ETL Pipeline Sample

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using Python. It extracts data from a CSV file, performs basic transformations (e.g., cleaning, deduplication), and loads the output into another CSV.

## Structure
- `main.py`: Orchestrates the ETL flow.
- `etl/extract.py`: Extracts data from a source file.
- `etl/transform.py`: Cleans, deduplicates, and formats data.
- `etl/load.py`: Loads transformed data to destination.
- `config/settings.yaml`: Holds paths and configurable variables.
- `tests/`: Contains a unit test for the transform logic.

## Tech Used
- Python 3.9+
- Pandas
- PyYAML (for config parsing)
- Pytest (for testing)

## How to Run
```bash
pip install -r requirements.txt
python main.py
