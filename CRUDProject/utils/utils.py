def validate_unique_id(receipts, receipt_id):
    return not any(receipt["id"] == receipt_id for receipt in receipts)
