import json
import sys
import time
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))


from app.core.llm_client import LLMClient, LLMError

from app.core.prompts_v1 import (
    SUMMARY_PROMPT as SUMMARY_PROMPT_V1,
    EXTRACTION_PROMPT as EXTRACTION_PROMPT_V1,
    CLASSIFICATION_PROMPT as CLASSIFICATION_PROMPT_V1,
)

from app.core.prompts_v2 import (
    SUMMARY_PROMPT as SUMMARY_PROMPT_V2,
    EXTRACTION_PROMPT as EXTRACTION_PROMPT_V2,
    CLASSIFICATION_PROMPT as CLASSIFICATION_PROMPT_V2,
)

from app.schemas.prompt_outputs import (
    SummaryOutput,
    ExtractionOutput,
    ClassificationOutput,
)

from app.services.output_validator import (
    OutputValidationError,
    validate_output,
)

from app.core.config import MODEL_NAME


DATASET_PATH = BASE_DIR / "evals" / "prompt_cases.json"
RESULTS_PATH = BASE_DIR / "evals" / "results.json"


PROMPT_CONFIG = {
    "v1": {
        "summary": SUMMARY_PROMPT_V1,
        "extraction": EXTRACTION_PROMPT_V1,
        "classification": CLASSIFICATION_PROMPT_V1,
    },
    "v2": {
        "summary": SUMMARY_PROMPT_V2,
        "extraction": EXTRACTION_PROMPT_V2,
        "classification": CLASSIFICATION_PROMPT_V2,
    },
}


TASK_MODELS = {
    "summary": SummaryOutput,
    "extraction": ExtractionOutput,
    "classification": ClassificationOutput,
}


def load_cases():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def build_prompt(case, prompt_version):
    task = case["task"]

    template = PROMPT_CONFIG[prompt_version][task]

    return template.format(
        document=case["input"]
    )


def run_case(client, case, prompt_version):
    task = case["task"]

    output_model = TASK_MODELS[task]

    result = {
        "case_id": case["case_id"],
        "task": task,
        "prompt_version": prompt_version,
        "model": MODEL_NAME,
        "latency_ms": None,
        "validation_result": "failed",
        "failure_category": None,
    }

    prompt = build_prompt(
        case,
        prompt_version
    )

    try:
        llm_response = client.generate(prompt)

        result["model"] = llm_response.model

        result["latency_ms"] = round(
            llm_response.latency_ms,
            2,
        )

        try:
            validate_output(
                llm_response.text,
                output_model,
            )

            result["validation_result"] = "passed"

        except OutputValidationError as exc:

            result["failure_category"] = str(
                exc
            ).split(":", 1)[0]

    except LLMError as exc:

        result["failure_category"] = "LLM_FAILURE"
        result["error"] = str(exc)

    except Exception as exc:

        result["failure_category"] = "UNEXPECTED_FAILURE"
        result["error"] = str(exc)

    return result


def save_results(results):

    with open(
        RESULTS_PATH,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False,
        )


def print_summary(results):

    for version in ["v1", "v2"]:

        version_results = [
            result
            for result in results
            if result["prompt_version"] == version
        ]

        passed = sum(
            1
            for result in version_results
            if result["validation_result"] == "passed"
        )

        failed = len(version_results) - passed

        latencies = [
            result["latency_ms"]
            for result in version_results
            if result["latency_ms"] is not None
        ]

        avg_latency = (
            sum(latencies) / len(latencies)
            if latencies
            else 0
        )

        print()
        print("-" * 60)
        print(f"VERSION {version.upper()}")
        print("-" * 60)

        print(f"Total cases : {len(version_results)}")
        print(f"Passed      : {passed}")
        print(f"Failed      : {failed}")
        print(f"Pass rate   : {(passed / len(version_results)) * 100:.1f}%")
        print(f"Avg latency : {avg_latency:.2f} ms")


def main():

    cases = load_cases()

    client = LLMClient()

    results = []

    print("=" * 60)
    print("PROMPT VERSION COMPARISON")
    print("=" * 60)

    print(f"Model: {MODEL_NAME}")
    print(f"Cases: {len(cases)}")
    print()

    for prompt_version in ["v1", "v2"]:

        print()
        print("=" * 60)
        print(f"RUNNING {prompt_version.upper()}")
        print("=" * 60)

        for case in cases:

            print(
                f"Running {case['case_id']} "
                f"({case['task']})..."
            )

            result = run_case(
                client,
                case,
                prompt_version,
            )

            results.append(result)

            print(
                f"  Validation: "
                f"{result['validation_result']}"
            )

            if result["latency_ms"] is not None:

                print(
                    f"  Latency: "
                    f"{result['latency_ms']} ms"
                )

            if result["failure_category"]:

                print(
                    f"  Failure: "
                    f"{result['failure_category']}"
                )

    save_results(results)

    print_summary(results)

    print()
    print("=" * 60)
    print("COMPARISON COMPLETE")
    print("=" * 60)

    print(f"Results saved to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()