import unittest
from calculator import hitung_diskon

class TestDiskonLanjut(unittest.TestCase):

    def test_diskon_float(self):
        # Diskon 33% dari 999
        hasil = hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_edge_case_harga_nol(self):
        hasil = hitung_diskon(0, 10)
        self.assertEqual(hasil, 0)

if __name__ == "__main__":
    unittest.main()

