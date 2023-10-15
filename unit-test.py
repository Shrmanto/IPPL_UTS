import unittest
from pengolah_data import hitung

class TestPengolahData(unittest. TestCase):
    def test_urutan_data(self):
        Result = [6,3,4,1,8,10,9]
        UrutanData = hitung(1, Result)
        self.assertEqual(UrutanData, [1, 3, 4, 6, 8, 9, 10])

    def test_urutan_data_2(self):
        Result = [6,3,4,1,8,10,9]
        UrutanData = hitung(1, Result)
        self.assertEqual(UrutanData, [3, 6, 9, 10, 8, 4, 1])

    def test_panjang_data(self):
        Result = [6,3,4,1,8,10,9]
        PanjangData = hitung(2, Result)
        self.assertEqual(PanjangData, 7)

    def test_maksimum_data(self):
        Result = [6,3,4,1,8,10,9]
        MaksimumData = hitung(3, Result)
        self.assertEqual(MaksimumData, 10)

    def test_minimum_data(self):
        Result = [6,3,4,1,8,10,9]
        MinimumData = hitung(4, Result)
        self.assertEqual(MinimumData, 1)

    def test_ratarata_data(self):
        Result = [6,3,4,1,8,10,9]
        RataRataData = hitung(5, Result)
        self.assertAlmostEqual(RataRataData, 5.86, places=2)

    def test_invalid_input(self):
        Result = [6,3,4,1,8,10,9]
        InvalidInput = hitung(6, Result)
        self.assertEqual(InvalidInput, 'Tidak Valid')

if __name__ == '__main__':
    unittest.main()