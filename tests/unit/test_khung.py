"""Kiểm tra khung dự án: các package import được, CI kết nối được Postgres."""

import importlib
import os

import psycopg
import pytest

PACKAGES = [
    "node",
    "node.inventory",
    "node.changelog",
    "node.replication",
    "node.recovery",
    "node.failure",
    "client",
]


@pytest.mark.parametrize("name", PACKAGES)
def test_import_package(name):
    importlib.import_module(name)


def test_ket_noi_postgres():
    url = os.environ.get("DATABASE_URL")
    if url is None:
        pytest.skip("Chưa đặt DATABASE_URL")
    with psycopg.connect(url) as conn:
        assert conn.execute("SELECT 1").fetchone() == (1,)
