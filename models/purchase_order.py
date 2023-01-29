from xia_fields import StringField, CompressedStringField
from xia_engine import Document
from xia_engine import ExternalField


class Customer(Document):
    id: str = StringField(description="Customer ID")
    name: str = StringField(description="Customer Name")
    description: str = CompressedStringField(description="Customer Description")


class PurchaseOrder(Document):
    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
    customer: str = StringField(description="Customer")
    customer_detail = ExternalField(document_type=Customer,
                                    description="Customer Detail",
                                    field_map={"customer": "id"})
