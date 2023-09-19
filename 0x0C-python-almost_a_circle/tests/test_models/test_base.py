#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_increment(self):
        """Test that the id attribute increments properly."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

        def test_id_manual_assignment(self):
            """Test that id can be manually assigned."""
            base = Base(100)
            self.assertEqual(base.id, 100)

            if __name__ == '__main__':
                unittest.main()
