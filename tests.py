"""
Brock Harman
CSCI 332 Spring 2026
Programming Assignment #class12
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main import get_orientation, on_segment, do_intersect


class TestSegmentIntersection(unittest.TestCase):

    def test_collinear(self):
        p = (1, 1)
        q = (2, 2)
        r = (3, 3)
        self.assertEqual(get_orientation(p, q, r), 0)

    def test_clockwise(self):
        p = (1, 1)
        q = (4, 4)
        r = (5, 2)
        self.assertEqual(get_orientation(p, q, r), 1)

    def test_counterclockwise(self):
        p = (1, 1)
        q = (4, 4)
        r = (2, 5)
        self.assertEqual(get_orientation(p, q, r), 2)

    def test_segment_true(self):
        p = (1, 1)
        q = (2, 2)
        r = (3, 3)
        self.assertTrue(on_segment(p, q, r))

    def test_segment_false(self):
        p = (1, 1)
        q = (5, 5)
        r = (3, 3)
        self.assertFalse(on_segment(p, q, r))

    def test_intersect_true(self):
        seg1 = ((1, 1), (4, 4))
        seg2 = ((2, 4), (4, 2))
        self.assertTrue(do_intersect(seg1, seg2))

    def test_intersect_false(self):
        seg1 = ((1, 1), (2, 2))
        seg2 = ((3, 3), (4, 4))
        self.assertFalse(do_intersect(seg1, seg2))


if __name__ == "__main__":
    unittest.main()
