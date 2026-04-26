def validate_status(response, expected_status):
    # Verify API returned expected HTTP status code
    assert response.status == expected_status, f"Expected {expected_status}, got {response.status}"


def validate_user_schema(user):
    # Ensure response contains all mandatory user fields
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "password" in user
    