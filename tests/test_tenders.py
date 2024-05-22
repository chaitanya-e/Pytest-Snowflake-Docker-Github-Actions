import pytest

@pytest.mark.tenders
def test_tender_amount(db_cursor):
    db_cursor.execute("SELECT tender_amount FROM H_tenders")
    result = db_cursor.fetchall()
    for row in result:
        assert row[0] > 0, f"tender_amount {row[0]} is not positive"

@pytest.mark.tenders
def test_non_null_store_id(db_cursor):
    db_cursor.execute("SELECT store_id FROM H_tenders")
    result = db_cursor.fetchall()
    for row in result:
        assert row[0] is not None, "store_id is None"
