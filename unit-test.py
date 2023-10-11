import unittest
from pengolah_data import urutan_data, panjang_data, maksimum_data, minimum_data, ratarata_data

class TestPengolahData(unittest. TestCase):
    def test_urutan_data(self):
        Result = [6,3,4,1,8,10,9]
        UrutanData = urutan_data(Result)
        self.assertEqual(UrutanData, [1, 3, 4, 6, 8, 9, 10])

    def test_urutan_data_2(self):
        Result = [6,3,4,1,8,10,9]
        UrutanData = urutan_data(Result)
        self.assertEqual(UrutanData, [3, 6, 9, 10, 8, 4, 1])

    def test_panjang_data(self):
        Result = [6,3,4,1,8,10,9]
        PanjangData = panjang_data(Result)
        self.assertEqual(PanjangData, 7)

    def test_maksimum_data(self):
        Result = [6,3,4,1,8,10,9]
        MaksimumData = maksimum_data(Result)
        self.assertEqual(MaksimumData, 10)

    def test_minimum_data(self):
        Result = [6,3,4,1,8,10,9]
        MinimumData = minimum_data(Result)
        self.assertEqual(MinimumData, 1)

    def test_ratarata_data(self):
        Result = [6,3,4,1,8,10,9]
        RataRataData = ratarata_data(Result)
        self.assertAlmostEqual(RataRataData, 5.86, places=2)

if __name__ == '__main__':
    unittest.main()