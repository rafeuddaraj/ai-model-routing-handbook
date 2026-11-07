import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import cost_calculator as cc  # noqa: E402


class AttemptCost(unittest.TestCase):
    def test_basic(self):
        # 80K in at $2/M + 15K out at $10/M = 0.16 + 0.15
        self.assertAlmostEqual(cc.attempt_cost(80_000, 15_000, 2, 10), 0.31)

    def test_cached_tokens_use_cached_price(self):
        full = cc.attempt_cost(100_000, 0, 2, 10)
        cached = cc.attempt_cost(100_000, 0, 2, 10, cached_tokens=50_000, cached_price=0.2)
        self.assertAlmostEqual(full, 0.2)
        self.assertAlmostEqual(cached, 0.11)

    def test_cached_price_defaults_to_input_price(self):
        self.assertAlmostEqual(cc.attempt_cost(100_000, 0, 2, 10, cached_tokens=40_000), 0.2)

    def test_rejects_negative_and_oversized_cache(self):
        with self.assertRaises(ValueError):
            cc.attempt_cost(-1, 0, 2, 10)
        with self.assertRaises(ValueError):
            cc.attempt_cost(1000, 0, 2, 10, cached_tokens=2000)


class CostPerAccepted(unittest.TestCase):
    def test_basic(self):
        self.assertAlmostEqual(cc.cost_per_accepted(0.31, 10, 0.6), 17.1833, places=3)

    def test_full_acceptance_is_just_the_sum(self):
        self.assertAlmostEqual(cc.cost_per_accepted(1, 2, 1), 3)

    def test_invalid_acceptance(self):
        for bad in (0, -0.1, 1.5):
            with self.assertRaises(ValueError):
                cc.cost_per_accepted(1, 1, bad)


class Demo(unittest.TestCase):
    def test_demo_numbers_match_the_handbook(self):
        rows = {r["name"].split()[0]: r for r in cc.demo_rows()}
        self.assertAlmostEqual(rows["Fast"]["hard"], 33.38, places=2)
        self.assertAlmostEqual(rows["Balanced"]["hard"], 17.18, places=2)
        self.assertAlmostEqual(rows["Strong"]["hard"], 13.27, places=2)
        self.assertAlmostEqual(rows["Fast"]["easy"], 11.13, places=2)
        self.assertAlmostEqual(rows["Balanced"]["easy"], 10.85, places=2)
        self.assertAlmostEqual(rows["Strong"]["easy"], 11.18, places=2)

    def test_cli_runs(self):
        self.assertEqual(cc.main(["--demo"]), 0)
        self.assertEqual(cc.main(["--input-tokens", "1000", "--output-tokens", "1000", "--input-price", "1",
                                  "--output-price", "1", "--acceptance", "0.5", "--json"]), 0)


if __name__ == "__main__":
    unittest.main()
