import razorpay
from app.core.config import settings


class RazorpayService:
    def __init__(self):
        self.client = razorpay.Client(auth=(settings.razorpay_key_id, settings.razorpay_key_secret))

    def create_order(self, amount: float, currency: str = "INR"):
        payload = {"amount": int(amount * 100), "currency": currency, "payment_capture": 1}
        return self.client.order.create(data=payload)
