## src/helpers/user_order_helper.py
import time

from src.pages.booking_page import BookingPage
from src.pages.dashboard_page import DashboardPage
from src.pages.equipment_page import EquipmentPage
from src.pages.order_summary_page import OrderSummaryPage
from src.pages.service_details_page import ServiceDetailsPage


class UserOrderHelper:
    @staticmethod
    def place_order(
        driver,

        equipment_categories=("Dump Trucks", "Dump 6 Trucks", "Dump Trucks Side Tipper"),
        company_name="",
        equipment_index=0,
        quantity=1,
        start_date="2025-07-18",
        end_date="2025-07-19",
        end_time="06:00 PM",
        payment_method="VISA"
    ):
        dashboard = DashboardPage(driver)
        for category in equipment_categories:
            dashboard.select_equipment_category(category)
        if company_name:
            dashboard.click_company(company_name)

        equipment = EquipmentPage(driver)
        equipment.select_equipment()
        equipment.click_continue()

        service = ServiceDetailsPage(driver)
        time.sleep(3)
        service.set_quantity(quantity)
        time.sleep(3)
        service.select_start_date(start_date)
        time.sleep(5)
        service.select_end_date(end_date)
        time.sleep(5)
        service.select_end_date(end_time)
        time.sleep(3)
        service.accept_terms()
        time.sleep(3)
        service.accept_rental_contracts()
        time.sleep(5)
        service.click_continue()
        time.sleep(3)

        order = OrderSummaryPage(driver)
        order.select_payment_method()
        order.click_pay_now()

        booking = BookingPage(driver)
        booking.verify_booking_success()

