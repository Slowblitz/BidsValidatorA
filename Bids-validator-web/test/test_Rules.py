import unittest
import BidsValidatorA as BVA
class Test_Rules(unittest.TestCase):

    def setUp(self):
        pass
    '''testing data rules'''
    def test_data_rules(self):
        list=["data"]
        self.assertEqual(BVA.is_data(list), True)
    def test_data_rules_1(self):
        list=["Data"]
        self.assertEqual(BVA.is_data(list), False)
    def test_data_rules_2(self):
        list=["dataa"]
        self.assertEqual(BVA.is_data(list), False)

    '''testing date rules'''
    def test_date_rules(self):
        list=["180116_001_m_enya_land-001"]
        self.assertEqual(BVA.is_date(list), True)
    def test_date_rules_1(self):
        list=["180116_m_enya_land-001"]
        self.assertEqual(BVA.is_date(list), False)
    def test_date_rules_2(self):
        list=["180116_001_m_land-001"]
        self.assertEqual(BVA.is_date(list), False)


    '''testing source rules'''
    def test_source_rules(self):
        list=["source"]
        self.assertEqual(BVA.is_source(list), True)
    def test_source_rules_1(self):
        list=["Source"]
        self.assertEqual(BVA.is_source(list), False)
    def test_source_rules_2(self):
        list=["sources"]
        self.assertEqual(BVA.is_source(list), False)

    '''testing subject rules'''
    def test_subject_rules(self):
        list=["sub-001"]
        self.assertEqual(BVA.is_sub(list), True)
    def test_subject_rules_1(self):
        list=["sub_001"]
        self.assertEqual(BVA.is_sub(list), False)
    def test_subject_rules_2(self):
        list=["Sub_001"]
        self.assertEqual(BVA.is_sub(list), False)

if __name__ == '__main__':
    unittest.main()
