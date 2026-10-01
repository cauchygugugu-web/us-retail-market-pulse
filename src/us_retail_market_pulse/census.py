from decimal import Decimal, InvalidOperation

import requests

MRTS_URL = "https://api.census.gov/data/timeseries/eits/mrts"

def build_mrts_params(year: int, category_code: str, api_key: str) -> dict[str, str]:
    return {
        "get": "time_slot_id,cell_value",
        "for": "us:*",
        "time": str(year),
        "data_type_code": "SM",
        "seasonally_adj": "yes",
        "category_code": category_code,
        "key": api_key,
    }

def fetch_mrts_response(year: int, category_code: str, api_key: str):
    params = build_mrts_params(year, category_code, api_key)
    try:
        response = requests.get(MRTS_URL, params=params, timeout=10)
    except requests.exceptions.Timeout:
        raise RuntimeError("Census MRTS request timed out") from None

    if response.status_code != 200:
        raise RuntimeError(f"Census MRTS returned HTTP {response.status_code}")
    return response

def parse_mrts_response(response):
    try:
        table = response.json()
    except ValueError:
        raise RuntimeError("Census MRTS response is not valid JSON") from None

    if not isinstance(table, list) or not table:
        raise RuntimeError("Census MRTS response is not a table")

    header = table[0]
    required = {
        "data_type_code",
        "time_slot_id",
        "seasonally_adj",
        "category_code",
        "cell_value",
    }

    if not isinstance(header, list) or not all(isinstance(name, str) for name in header):
        raise RuntimeError("Census MRTS response has an invalid header")
    if len(header) != len(set(header)) or not required.issubset(header):
        raise RuntimeError("Census MRTS response has missing or duplicate columns")

    rows = []
    for row in table[1:]:
        if not isinstance(row, list) or len(row) != len(header):
            raise RuntimeError("Census MRTS response has an invalid row")
        rows.append(dict(zip(header, row, strict=True)))

    return rows

def validate_mrts_rows(
        rows: list[dict[str, str]],
        year: int,
        category_code: str,
) -> list[dict[str, str]]:
    required = {
        "time_slot_id",
        "cell_value",
        "time",
        "data_type_code",
        "seasonally_adj",
        "category_code",
        "us",
    }
    expected_months = {
        f"{year}-{month:02d}"
        for month in range(1, 13)
    }
    expected_month_order = [
        f"{year}-{month:02d}"
        for month in range(1, 13)
    ]
    actual_months = []

    if len(rows) != 12:
        raise RuntimeError("Census MRTS response does not contain 12 monthly rows")

    for row in rows:
        if not required.issubset(row):
            raise RuntimeError("Census MRTS response has missing fields")

        if any(
            row[field] is None
            or (
                isinstance(row[field], str)
                and row[field].strip() == ""
            )
            for field in required
        ):
            raise RuntimeError("Census MRTS row has missing values")

        if row["category_code"] != category_code:
            raise RuntimeError("Census MRTS row has an unexpected category_code")
        if row["data_type_code"] != "SM":
            raise RuntimeError("Census MRTS row has an unexpected data type")
        if row["seasonally_adj"] != "yes":
            raise RuntimeError("Census MRTS row has an unexpected adjustment status")
        if row["us"] != "1":
            raise RuntimeError("Census MRTS row has an unexpected geography")

        try:
            numeric_value = Decimal(row["cell_value"])
        except (InvalidOperation, TypeError):
            raise RuntimeError("Census MRTS row has a nonnumeric value") from None

        if not numeric_value.is_finite():
            raise RuntimeError("Census MRTS row has a nonfinite value")

        actual_months.append(row["time"])

    if len(actual_months) != len(set(actual_months)):
        raise RuntimeError("Census MRTS response has duplicate months")

    if set(actual_months) != expected_months:
        raise RuntimeError("Census MRTS response has missing or unexpected months")

    if actual_months != expected_month_order:
        raise RuntimeError("Census MRTS response is not in chronological order")

    return rows