# =====================================================================
# TC_LOG_01 & TC_LOG_02: Boundary Value Analysis for Username Length
# Valid Username Length: 5 to 15 characters
# =====================================================================

def validate_username(username: str) -> bool:
    """Validates if username length satisfies BVA requirements (5 - 15 chars)."""
    return 5 <= len(username) <= 15


def test_valid_username_lower_boundary():
    # Boundary: Exactly 5 characters
    assert validate_username("user1") == True, "Failed: 5-character username should be valid"
    print("✓ PASS: Lower boundary (5 chars)")


def test_invalid_username_too_short():
    # Boundary: 4 characters
    assert validate_username("user") == False, "Failed: 4-character username should be rejected"
    print("✓ PASS: Off-by-one lower boundary (4 chars)")


def test_valid_username_upper_boundary():
    # Boundary: Exactly 15 characters
    assert validate_username("a1b2c3d4e5f6g7h") == True, "Failed: 15-character username should be valid"
    print("✓ PASS: Upper boundary (15 chars)")


if __name__ == "__main__":
    print("\n--- Running Automated BVA Test Suite ---")
    test_valid_username_lower_boundary()
    test_invalid_username_too_short()
    test_valid_username_upper_boundary()
    print("--- All Tests Executed Successfully ---\n")