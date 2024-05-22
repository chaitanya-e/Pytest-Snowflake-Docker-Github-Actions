import pytest

@pytest.mark.locations
def test_address_completeness(db_cursor):
    db_cursor.execute("SELECT address1, city, state, zip FROM h_locations")
    result = db_cursor.fetchall()
    for row in result:
        assert row[0] is not None, "address1 is None"
        assert row[1] is not None, "city is None"
        assert row[2] is not None, "state is None"
        assert row[3] is not None, "zip is None"

@pytest.mark.locations
def test_latitude_longitude(db_cursor):
    db_cursor.execute("SELECT latitude, longitude FROM h_locations")
    result = db_cursor.fetchall()
    for row in result:
        assert -90 <= row[0] <= 90, f"latitude {row[0]} out of range"
        assert -180 <= row[1] <= 180, f"longitude {row[1]} out of range"
