from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Plamen', 1.00)

    def test_correct_initialization(self):
        self.assertEqual('Plamen', self.driver.name)
        self.assertEqual(1.00, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_cant_be_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_earned_money_setter(self):
        self.assertEqual(self.driver.earned_money, 0)

        self.driver.earned_money += 5

        self.assertEqual(self.driver.earned_money, 5)

    def test_add_cargo_offer_that_is_already_add_raises_exception(self):
        self.driver.add_cargo_offer('Sofia', 5)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Sofia', 5)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_successfully_returns_string(self):
        result = self.driver.add_cargo_offer('Sofia', 5)

        self.assertEqual(result, "Cargo for 5 to Sofia was added as an offer.")

    def test_drive_best_cargo_no_offers_available_returns_string(self):
        self.assertEqual(self.driver.available_cargos, {})

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer_with_no_activities(self):
        self.driver.add_cargo_offer('Sofia', 200)
        self.driver.add_cargo_offer('Stara Zagora', 50)
        self.driver.add_cargo_offer('Varna', 100)

        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

        res = self.driver.drive_best_cargo_offer()

        self.assertEqual(res, "Plamen is driving 200 to Sofia.")

    def test_eat_reduce_earned_money(self):
        self.driver.earned_money = 50

        self.driver.eat(250)

        self.assertEqual(self.driver.earned_money, 30)

    def test_sleep_reduce_earned_money(self):
        self.driver.earned_money = 50

        self.driver.sleep(1000)

        self.assertEqual(self.driver.earned_money, 5)

    def test_pump_gas_reduce_earned_money(self):
        self.driver.earned_money = 550

        self.driver.pump_gas(1500)

        self.assertEqual(self.driver.earned_money, 50)

    def test_repair_truck_reduce_earned_money(self):
        self.driver.earned_money = 8000

        self.driver.repair_truck(10000)

        self.assertEqual(self.driver.earned_money, 500)

    def test_repr_method(self):
        result = str(self.driver)
        result_repr = repr(self.driver)

        self.assertEqual(result, result_repr)

        self.assertEqual(result, "Plamen has 0 miles behind his back.")

    def test_check_for_activities(self):
        self.driver.earned_money = 11760

        res = self.driver.check_for_activities(10000)
        self.assertEqual(res, None)
        self.assertEqual(self.driver.earned_money, 10)

    def test_drive_best_offer_with_activities(self):
        self.driver.earned_money = 11760

        need_money_for_cargo = 11750
        km_to_drive = 10000
        money_to_earn = self.driver.money_per_mile * km_to_drive

        self.driver.add_cargo_offer('Sofia', km_to_drive)
        self.driver.drive_best_cargo_offer()

        expected_money_left = (11760 + money_to_earn) - need_money_for_cargo
        self.assertEqual(self.driver.earned_money, expected_money_left)

    def test_drive_best_offer_with_activities_money_ends(self):
        self.driver.earned_money = 11760 - 10011

        need_money_for_cargo = 11750
        km_to_drive = 10000
        money_to_earn = self.driver.money_per_mile * km_to_drive

        self.driver.add_cargo_offer('Sofia', km_to_drive)
        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), "Plamen went bankrupt.")


