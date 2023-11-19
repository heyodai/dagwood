import pytest
from dagwood.http_codes import ResponseTypes, get_enums, interpret


# Test known response codes
@pytest.mark.parametrize(
    "code, expected_message, expected_explanation, expected_type",
    [
        (200, "OK", "The request has succeeded.", ResponseTypes.SUCCESS),
        (
            404,
            "Not Found",
            "The server can not find the requested resource.",
            ResponseTypes.CLIENT_ERROR,
        ),
        (
            500,
            "Internal Server Error",
            "The server has encountered a situation it does not know how to handle.",
            ResponseTypes.SERVER_ERROR,
        ),
    ],
)
def test_interpret_known_codes(
    code, expected_message, expected_explanation, expected_type
):
    response = interpret(code)
    assert response.message == expected_message
    assert response.explanation == expected_explanation
    assert response.type == expected_type


# Test unknown response codes
def test_interpret_unknown_code():
    unknown_code = 999
    response = interpret(unknown_code)
    assert response.message == "Unknown"
    assert response.explanation == "No description available."
    assert response.type == "Unknown"


# Test get_enums function
def test_get_enums():
    expected_types = [
        ResponseTypes.INFO,
        ResponseTypes.SUCCESS,
        ResponseTypes.REDIRECT,
        ResponseTypes.CLIENT_ERROR,
        ResponseTypes.SERVER_ERROR,
    ]
    assert set(get_enums()) == set(expected_types)
