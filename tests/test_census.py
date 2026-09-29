import unittest
from urllib.parse import parse_qs, urlparse

from us_retail_market_pulse.census import (
    build_eits_url,
    build_time_range,
    parse_census_table,
)


class TimeRangeTests(unittest.TestCase):
    def test_open_ended_range(self) -> None:
        self.assertEqual(build_time_range("2012-01"), "from 2012-01")

    def test_closed_range(self) -> None:
        self.assertEqual(build_time_range("2012-01", "2020-12"), "from 2012-01 to 2020-12")


class UrlBuilderTests(unittest.TestCase):
    def test_builds_bounded_url_without_exposing_key(self) -> None:
        url = build_eits_url(
            "mrts",
            ["cell_value", "category_code"],
            start="2019-01",
            end="2019-12",
            predicates={"seasonally_adj": "yes"},
        )
        parsed = urlparse(url)
        query = parse_qs(parsed.query)

        self.assertTrue(parsed.path.endswith("/mrts"))
        self.assertEqual(query["get"], ["cell_value,category_code"])
        self.assertEqual(query["time"], ["from 2019-01 to 2019-12"])
        self.assertEqual(query["seasonally_adj"], ["yes"])
        self.assertNotIn("key", query)

    def test_rejects_unknown_program(self) -> None:
        with self.assertRaises(ValueError):
            build_eits_url("unknown", ["cell_value"], start="2019")


class CensusParserTests(unittest.TestCase):
    def test_parses_array_response(self) -> None:
        payload = [
            ["time", "cell_value", "category_code"],
            ["2024-01", "100.0", "example"],
            ["2024-02", "102.0", "example"],
        ]

        self.assertEqual(
            parse_census_table(payload),
            [
                {"time": "2024-01", "cell_value": "100.0", "category_code": "example"},
                {"time": "2024-02", "cell_value": "102.0", "category_code": "example"},
            ],
        )

    def test_rejects_malformed_rows(self) -> None:
        with self.assertRaises(ValueError):
            parse_census_table([["time", "value"], ["2024-01"]])


if __name__ == "__main__":
    unittest.main()

