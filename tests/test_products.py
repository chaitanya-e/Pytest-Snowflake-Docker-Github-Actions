import pytest
@pytest.mark.products
def test_unique_product_key(db_cursor):
    db_cursor.execute("SELECT product_key FROM H_products")
    result = db_cursor.fetchall()
    product_keys = [row[0] for row in result]
    assert len(product_keys) == len(set(product_keys)), "Duplicate product_key found"
