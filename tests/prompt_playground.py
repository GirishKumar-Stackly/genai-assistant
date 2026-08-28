import json
from pathlib import Path


DATASET_PATH = Path("evals/prompt_cases.json")


def test_prompt_dataset_exists():
    assert DATASET_PATH.exists()


def test_prompt_dataset_has_10_cases():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        cases = json.load(file)

    assert len(cases) == 10


def test_case_ids_are_unique():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        cases = json.load(file)

    case_ids = [case["case_id"] for case in cases]

    assert len(case_ids) == len(set(case_ids))


def test_all_cases_have_required_fields():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        cases = json.load(file)

    required_fields = {
        "case_id",
        "task",
        "input",
        "expected_structure",
        "expected_values",
    }

    for case in cases:
        assert required_fields.issubset(case.keys())


def test_tasks_are_valid():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        cases = json.load(file)

    allowed_tasks = {
        "summary",
        "extraction",
        "classification",
    }

    for case in cases:
        assert case["task"] in allowed_tasks