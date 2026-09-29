"""Small, source-transparent helpers for the Census EITS API.

The first milestone deliberately keeps this client generic. Exact MRTS fields and
category predicates will be added only after they are verified against official
metadata.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping, Sequence
from urllib.parse import urlencode
from urllib.request import urlopen


EITS_BASE_URL = "https://api.census.gov/data/timeseries/eits"
SUPPORTED_PROGRAMS = frozenset({"mrts", "mwts"})


def build_time_range(start: str, end: str | None = None) -> str:
    """Return a Census EITS time predicate.

    Dates may be a year (``2019``) or a year-month (``2019-01``). Validation is
    intentionally light here; source-specific validation will be added after the
    official series grain has been confirmed.
    """

    if not start or not start.strip():
        raise ValueError("start must be a non-empty year or year-month")
    start = start.strip()

    if end is None:
        return f"from {start}"
    if not end.strip():
        raise ValueError("end must be a non-empty year or year-month")
    return f"from {start} to {end.strip()}"


def build_eits_url(
    program: str,
    fields: Iterable[str],
    *,
    start: str,
    end: str | None = None,
    predicates: Mapping[str, str] | None = None,
    api_key: str | None = None,
) -> str:
    """Build a Census EITS request URL without making a network call."""

    normalized_program = program.lower().strip()
    if normalized_program not in SUPPORTED_PROGRAMS:
        supported = ", ".join(sorted(SUPPORTED_PROGRAMS))
        raise ValueError(f"Unsupported program {program!r}; expected one of: {supported}")

    selected_fields = [field.strip() for field in fields if field.strip()]
    if not selected_fields:
        raise ValueError("At least one field is required")

    parameters: dict[str, str] = {
        "get": ",".join(selected_fields),
        "time": build_time_range(start, end),
    }
    if predicates:
        parameters.update({key: value for key, value in predicates.items()})
    if api_key:
        parameters["key"] = api_key

    return f"{EITS_BASE_URL}/{normalized_program}?{urlencode(parameters)}"


def parse_census_table(payload: Sequence[Sequence[object]]) -> list[dict[str, object]]:
    """Convert the Census array-of-arrays response into row dictionaries."""

    if not payload:
        return []

    header = [str(value) for value in payload[0]]
    if len(header) != len(set(header)):
        raise ValueError("Census response contains duplicate column names")

    rows: list[dict[str, object]] = []
    for row_number, row in enumerate(payload[1:], start=2):
        if len(row) != len(header):
            raise ValueError(
                f"Row {row_number} has {len(row)} values; expected {len(header)}"
            )
        rows.append(dict(zip(header, row, strict=True)))
    return rows


def fetch_eits_json(url: str, *, timeout_seconds: int = 30) -> list[dict[str, object]]:
    """Fetch and parse one already-bounded Census EITS request."""

    with urlopen(url, timeout=timeout_seconds) as response:  # noqa: S310
        payload = json.load(response)
    return parse_census_table(payload)

