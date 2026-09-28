import json, argparse, sys

def validate_annotation(item):
    errors = []
    if 'prompt_id' not in item:
        errors.append("Missing prompt_id")
    if item.get('chosen_response') not in ['Response A', 'Response B', 'TIE']:
        errors.append("Invalid chosen_response")
    if len(item.get('rationale', '')) < 20:
        errors.append("Rationale must be at least 20 characters long")
    scores = item.get('dimension_scores', {})
    for dim in ['helpfulness', 'harmlessness', 'honesty', 'reasoning', 'style']:
        val = scores.get(dim)
        if not isinstance(val, int) or val < 1 or val > 5:
            errors.append(f"Invalid dimension score for {dim}: {val}")
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate RLHF Annotations")
    parser.add_argument("--dataset", required=True, help="Path to JSON dataset")
    args = parser.parse_args()

    with open(args.dataset) as f:
        data = json.load(f)

    total_errors = 0
    for idx, item in enumerate(data):
        errs = validate_annotation(item)
        if errs:
            print(f"Item {idx} ({item.get('prompt_id')}): INVALID -> {errs}")
            total_errors += len(errs)
        else:
            print(f"Item {idx} ({item.get('prompt_id')}): VALID")

    if total_errors == 0:
        print("\nAll annotations passed schema and validation rules!")
        sys.exit(0)
    else:
        print(f"\nFailed with {total_errors} errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
