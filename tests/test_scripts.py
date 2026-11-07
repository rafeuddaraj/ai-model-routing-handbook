import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import summarize_decision_log as sdl  # noqa: E402
import token_ratio as tr  # noqa: E402


def write_csv(rows, header):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="", encoding="utf-8")
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
    f.close()
    return f.name


class TokenRatio(unittest.TestCase):
    def test_ratios_and_summary(self):
        p = write_csv([[1, 100, 300], [2, 200, 400], [3, "", ""]], ["passage", "english_tokens", "other_tokens"])
        try:
            rows = tr.load_rows(p)
            self.assertEqual(len(rows), 2)  # unfilled row skipped
            s = tr.summarize(rows)
            self.assertAlmostEqual(s["mean"], 2.5)
            self.assertAlmostEqual(s["total_ratio"], 700 / 300)
        finally:
            os.unlink(p)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            tr.summarize([])


class DecisionLog(unittest.TestCase):
    HEADER = ["date", "task", "phase", "tier", "result", "rework_minutes", "escalated"]

    def test_groups_by_phase_and_tier(self):
        p = write_csv([
            ["d", "t", "implement", "balanced", "accepted", 0, "no"],
            ["d", "t", "implement", "balanced", "accepted_with_rework", 20, "no"],
            ["d", "t", "implement", "fast", "rejected", 30, "yes"],
        ], self.HEADER)
        try:
            out = {(s["phase"], s["tier"]): s for s in sdl.summarize(sdl.load(p))}
            b = out[("implement", "balanced")]
            self.assertEqual(b["n"], 2)
            self.assertAlmostEqual(b["first_time_rate"], 0.5)
            self.assertAlmostEqual(b["avg_rework_min"], 10.0)
            self.assertEqual(out[("implement", "fast")]["escalations"], 1)
        finally:
            os.unlink(p)

    def test_example_file_in_repo_parses(self):
        path = os.path.join(os.path.dirname(__file__), "..", "templates", "decision-log.example.csv")
        self.assertGreater(len(sdl.summarize(sdl.load(path))), 0)


if __name__ == "__main__":
    unittest.main()
