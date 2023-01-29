from xia_fields import StringField
from xia_engine import Document


class PurchaseOrder(Document):
    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
