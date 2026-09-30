from unittest.mock import Mock, patch

import pytest
from requests.exceptions import Timeout

from us_retail_market_pulse.census import (
    MRTS_URL,
    build_mrts_params,
    fetch_mrts_response,
    parse_mrts_response,
)


def test_build_mrts_params():
    params = build_mrts_params(2024, "441", "test-key")

    assert params["time"] == "2024"
    assert params["category_code"] == "441"
    assert params["for"] == "us:*"
    assert params["data_type_code"] == "SM"
    assert params["seasonally_adj"] == "yes"
    assert params["key"] == "test-key"

def test_fetch_mrts_response_without_network():
    fake_response = Mock(status_code=200)

    with patch(
        "us_retail_market_pulse.census.requests.get",
        return_value=fake_response,
    ) as fake_get:
        result = fetch_mrts_response(year=2024, category_code="441", api_key="test-key")

        assert result is fake_response
        fake_get.assert_called_once_with(
            MRTS_URL,
            params=build_mrts_params(2024, "441", "test-key"),
            timeout=10,
        )

def test_fetch_mrts_response_non_200_hides_api_key():
    fake_key = "test-secret-key"
    fake_response = Mock(status_code=503)

    with patch(
        "us_retail_market_pulse.census.requests.get",
        return_value=fake_response,
    ):
        with pytest.raises(RuntimeError) as error:
            fetch_mrts_response(2024, "441", fake_key)

    message = str(error.value)
    assert "HTTP 503" in message
    assert fake_key not in message
    assert MRTS_URL not in message

def test_fetch_mrts_response_timeout_hides_api_key():
    fake_key = "test-secret-key"

    with patch(
        "us_retail_market_pulse.census.requests.get",
        side_effect=Timeout(f"Time out: {MRTS_URL}?key={fake_key}"),
    ):
        with pytest.raises(RuntimeError) as error:
            fetch_mrts_response(2024, "441", fake_key)

    message = str(error.value)
    assert "timed out" in message.lower()
    assert fake_key not in message
    assert MRTS_URL not in message

def test_parse_mrts_response_valid_table():
    fake_response = Mock()
    fake_response.json.return_value = [
        [
            "data_type_code",
            "time_slot_id",
            "seasonally_adj",
            "category_code",
            "cell_value",
        ],
        ["SM", "01", "yes", "441", "12345"],
    ]

    rows = parse_mrts_response(fake_response)

    assert rows == [
        {
            "data_type_code": "SM",
            "time_slot_id": "01",
            "seasonally_adj": "yes",
            "category_code": "441",
            "cell_value": "12345",
        }
    ]

def test_parse_mrts_response_missing_required_column():
    fake_key = "test-secret-key"
    fake_response = Mock()
    fake_response.json.return_value = [
        ["data_type_code", "time_slot_id", "seasonally_adj", "category_code", "debug"],
        ["SM", "01", "yes", "441", fake_key],
    ]

    with pytest.raises(RuntimeError) as error:
        parse_mrts_response(fake_response)

    message = str(error.value)
    assert "missing" in message.lower()
    assert fake_key not in message
    assert MRTS_URL not in message

def test_parse_mrts_response_rejects_wrong_row_length():
    fake_response = Mock()
    fake_response.json.return_value = [
        [
            "data_type_code",
            "time_slot_id",
            "seasonally_adj",
            "category_code",
            "cell_value",
        ],
        ["SM", "01", "yes", "441"],
    ]

    with pytest.raises(RuntimeError) as error:
        parse_mrts_response(fake_response)

    assert "invalid row" in str(error.value).lower()

def test_parse_mrts_response_invalid_json():
    fake_key = "test-secret-key"
    fake_response = Mock()
    fake_response.json.side_effect = ValueError(
        f"Bad JSON from {MRTS_URL}?key={fake_key}"
    )

    with pytest.raises(RuntimeError) as error:
        parse_mrts_response(fake_response)

    message = str(error.value)
    assert "not valid json" in message.lower()
    assert fake_key not in message
    assert MRTS_URL not in message