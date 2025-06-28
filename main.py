from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import yaml

def load_config(path="config/settings.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    raw_data = extract_data(config["input_path"])
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, config["output_path"])

if __name__ == "__main__":
    main()
