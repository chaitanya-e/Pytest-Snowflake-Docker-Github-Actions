import pytest

@pytest.mark.itemcosts
def test_itemcosts_data_integrity(db_cursor):
    db_cursor.execute("SELECT product_key, day_date, store_id, unit_cost, date_extracted FROM H_ITEMCOSTS")
    result = db_cursor.fetchall()
    for row in result:
        assert row[0] is not None, "product_key is None"
        assert row[1] is not None, "day_date is None"
        assert row[2] is not None, "store_id is None"
        assert row[3] is not None and row[3] > 0, "unit_cost is not positive"
        assert row[4] is not None, "date_extracted is None"
