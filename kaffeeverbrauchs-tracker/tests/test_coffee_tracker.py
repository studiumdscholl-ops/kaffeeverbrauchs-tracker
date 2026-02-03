import unittest
from src.coffee_tracker import CoffeeTracker


class CoffeeTrackerTest(unittest.TestCase):
    """
    Unit-Tests für die Klasse CoffeeTracker
    """

    def setUp(self):
        """
        Wird vor jedem Test aufgerufen.
        Erstellt eine frische Tracker-Instanz,
        damit Tests unabhängig voneinander sind.
        """
        self.tracker = CoffeeTracker(daily_limit=2)

    def test_add_coffee_increases_count(self):
        """Getestet wird ob die Eingabe den Zähler erhöht"""
        self.tracker.add_coffee(200)
        self.assertEqual(self.tracker.coffee_count(), 1)

    def test_total_coffee_ml(self):
        """Testet die Berechnung der gesamten Kaffeemenge."""
        self.tracker.add_coffee(200)
        self.tracker.add_coffee(150)
        self.assertEqual(self.tracker.total_coffee_ml(), 350)

    def test_limit_exceeded(self):
        """Testet, ob das Tageslimit korrekt überschritten wird."""
        self.tracker.add_coffee(200)
        self.tracker.add_coffee(150)
        self.tracker.add_coffee(100)
        self.assertTrue(self.tracker.limit_exceeded())

    def test_average_coffee_size(self):
        """Testet die Berechnung der durchschnittlichen Tassengröße."""
        self.tracker.add_coffee(200)
        self.tracker.add_coffee(100)
        self.assertEqual(self.tracker.average_coffee_size(), 150)

    def test_average_empty_list(self):
        """Testet den Durchschnitt ohne Einträge."""
        self.assertEqual(self.tracker.average_coffee_size(), 0)

    def test_invalid_coffee_size_raises_error(self):
        """Testet, ob ungültige Eingaben korrekt abgefangen werden."""
        with self.assertRaises(ValueError):
            self.tracker.add_coffee(-50)


if __name__ == "__main__":
    unittest.main()

