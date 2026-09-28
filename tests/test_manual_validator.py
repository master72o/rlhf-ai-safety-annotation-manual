import json, os, sys, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validator import validate_annotation

def test_gold_dataset_validity():
    gold_path = os.path.join(os.path.dirname(__file__), '../data/gold_calibration_dataset.json')
    with open(gold_path) as f:
        data = json.load(f)
    assert len(data) >= 2
    for item in data:
        errs = validate_annotation(item)
        assert len(errs) == 0

def test_invalid_annotation_detection():
    bad_item = {
        "prompt_id": "BAD-01",
        "chosen_response": "Invalid Choice",
        "rationale": "Too short",
        "dimension_scores": {"helpfulness": 10}
    }
    errs = validate_annotation(bad_item)
    assert len(errs) > 0
