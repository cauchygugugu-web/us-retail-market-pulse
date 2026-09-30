import requests

MRTS_URL = "https://api.census.gov/data/timeseries/eits/mrts"

def build_mrts_params(year: int, category_code: str, api_key: str) -> dict[str, str]:
    return {
        "get": "data_type_code,time_slot_id,seasonally_adj,category_code,cell_value",
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