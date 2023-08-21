import pytest
from unittest.mock import MagicMock
from products_api.controllers import main_router


@pytest.mark.products
def test_list_products(client):
    mock_products_repo = MagicMock()
    mock_products_repo.list.return_value = [
        {"id": "1", "name": "Product 1"},
        {"id": "2", "name": "Product 2"},
    ]
    mock_products_repo.count.return_value = 2
    mock_products_repo.count_removed.return_value = 0

    main_router.dependencies[0].override = MagicMock(return_value=mock_products_repo)

    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data["error"] is False
    assert data["items"][0]["name"] == "Product 1"
    assert data["items"][1]["name"] == "Product 2"


@pytest.mark.products
def test_show_product(client):
    mock_products_repo = MagicMock()
    mock_products_repo.find_by_id.return_value = {"id": "1", "name": "Product 1"}

    main_router.dependencies[1].override = MagicMock(return_value=mock_products_repo)

    response = client.get("/1_products")

    assert response.status_code == 200
    data = response.json()
    assert data["error"] is False
    assert data["item"]["name"] == "Product 1"


@pytest.mark.products
def test_create_product(client):
    mock_products_repo = MagicMock()
    mock_products_repo.create.return_value = {"id": "1", "name": "New Product"}

    main_router.dependencies[2].override = MagicMock(return_value=mock_products_repo)

    product_data = {"name": "New Product"}
    response = client.post("/", json=product_data)

    assert response.status_code == 200
    data = response.json()
    assert data["error"] is False
    assert data["detail"] == "Product created successfully"
    assert data["item"]["name"] == "New Product"


@pytest.mark.products
def test_update_product(client):
    mock_products_repo = MagicMock()
    mock_products_repo.update.return_value = {"id": "1", "name": "Updated Product"}

    main_router.dependencies[3].override = MagicMock(return_value=mock_products_repo)

    product_data = {"name": "Updated Product"}
    response = client.put("/1_product", json=product_data)

    assert response.status_code == 200
    data = response.json()
    assert data["error"] is False
    assert data["detail"] == "Product updated successfully"
    assert data["item"]["name"] == "Updated Product"


@pytest.mark.products
def test_delete_product(client):
    mock_products_repo = MagicMock()
    main_router.dependencies[4].override = MagicMock(return_value=mock_products_repo)

    response = client.delete("/1_product")

    assert response.status_code == 200
    data = response.json()
    assert data["error"] is False
    assert data["detail"] == "Product deleted successfully"
