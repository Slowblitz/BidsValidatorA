import unittest
import BidsValidatorA as BVA
import json
import os
PATH=os.getcwd()


class test_bids(unittest.TestCase):

    
    def setUp(self):
        pass
    '''testing bids folder'''

    def test_bids_dataset_1(self):
        names=list()
        test1="Tests/DataSets/ds001/Data"
        dic_data = json.loads(
        json.dumps(BVA.path_hierarchy(test1), indent=2, sort_keys=True))
        names = BVA.get_name_in_dir([dic_data], names)
        self.assertEqual(BVA.is_bids(names), False)

    def test_bids_dataset_2(self):
        names=list()
        test1="Tests/DataSets/ds002/data"
        dic_data = json.loads(
        json.dumps(BVA.path_hierarchy(test1), indent=2, sort_keys=True))
        names = BVA.get_name_in_dir([dic_data], names)
        self.assertEqual(BVA.is_bids(names), True)

    def test_bids_dataset_3(self):
        names=list()
        test1="Tests/DataSets/ds003/data"
        dic_data = json.loads(
        json.dumps(BVA.path_hierarchy(test1), indent=2, sort_keys=True))
        names = BVA.get_name_in_dir([dic_data], names)
        self.assertEqual(BVA.is_bids(names), False)

    def test_bids_dataset_4(self):
        names=list()
        test1="Tests/DataSets/ds004/data"
        dic_data = json.loads(
        json.dumps(BVA.path_hierarchy(test1), indent=2, sort_keys=True))
        names = BVA.get_name_in_dir([dic_data], names)
        self.assertEqual(BVA.is_bids(names), False)

    def test_bids_dataset_5(self):
        names=list()
        test1="Tests/DataSets/ds005/data"
        dic_data = json.loads(
        json.dumps(BVA.path_hierarchy(test1), indent=2, sort_keys=True))
        names = BVA.get_name_in_dir([dic_data], names)
        self.assertEqual(BVA.is_bids(names), False)
    
 
if __name__ == '__main__':
    unittest.main()
 
