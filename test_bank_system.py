import runpy
import unittest
from unittest.mock import patch

import semi_file_1
import semi_file_2


class BankSystemTests(unittest.TestCase):
    def test_add_customer_stores_valid_customer_record(self):
        customers = []
        inputs = [
            "1",
            "C001",
            "Alice",
            "Main Street",
            "1234567890",
            "alice@example.com",
            "ACC101",
            "Savings",
            "1500.50",
        ]

        with patch("builtins.input", side_effect=inputs):
            result = semi_file_1.add_customer(customers)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["customer_id"], "C001")
        self.assertEqual(result[0]["account_balance"], 1500.5)

    def test_remove_customer_removes_matching_id(self):
        customers = [{
            "customer_id": "C001",
            "customer_name": "Alice",
            "customer_address": "Main Street",
            "customer_phone": 1234567890,
            "customer_email": "alice@example.com",
            "account_number": "ACC101",
            "account_type": "Savings",
            "account_balance": 1500.5,
        }]

        with patch("builtins.input", return_value="C001"):
            result = semi_file_1.remove_customer(customers)

        self.assertEqual(result, [])

    def test_update_customer_changes_target_record(self):
        customers = [{
            "customer_id": "C001",
            "customer_name": "Alice",
            "customer_address": "Main Street",
            "customer_phone": 1234567890,
            "customer_email": "alice@example.com",
            "account_number": "ACC101",
            "account_type": "Savings",
            "account_balance": 1500.5,
        }]

        inputs = [
            "C001",
            "Alice Updated",
            "New Street",
            "9876543210",
            "alice.new@example.com",
            "ACC999",
            "Checking",
            "2200.75",
        ]

        with patch("builtins.input", side_effect=inputs):
            result = semi_file_1.update_customer(customers)

        self.assertEqual(result[0]["customer_name"], "Alice Updated")
        self.assertEqual(result[0]["account_balance"], 2200.75)

    def test_main_accepts_exit_command(self):
        script = runpy.run_path("/workspaces/Bank-Interface-System-/#bank interface system.py")

        with patch("builtins.input", side_effect=["exit"]):
            script["main"]()

    def test_customer_data_is_persisted_to_json_files(self):
        customers = [{
            "customer_id": "C101",
            "customer_name": "Bob",
            "customer_address": "Second Street",
            "customer_phone": 5551234567,
            "customer_email": "bob@example.com",
            "account_number": "ACC202",
            "account_type": "Checking",
            "account_balance": 2000.0,
        }]

        import tempfile
        import os

        with tempfile.TemporaryDirectory() as temp_dir:
            semi_file_1.save_customers(customers, temp_dir)
            self.assertTrue(os.path.exists(os.path.join(temp_dir, "customers.json")))
            self.assertTrue(os.path.exists(os.path.join(temp_dir, "C101.json")))
            reloaded = semi_file_1.load_customers(temp_dir)
            self.assertEqual(reloaded[0]["customer_id"], "C101")


if __name__ == "__main__":
    unittest.main()
