import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.extract import extract_function

def transform_function():
    raw_df = extract_function()
    selected_data = raw_df[["Type", "Primary Breed", "Outcome Status", "Days in Shelter"]]
    formatted_records = (
        selected_data
        .where(raw_df.notna(), other='')
        .rename(
            columns={
                "Type": "animal_type",
                "Primary Breed": "breed",
                "Outcome Status": "outcome",
                "Days in Shelter": "days_in_shelter",
            }
        )
        .to_dict("records")
    )

    records = [{k:v.lower() if isinstance(v, str) else v for k, v in record.items()} for record in formatted_records]
    return records