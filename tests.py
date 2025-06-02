import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def testCalcWithCurrentDir(self):
        result = get_files_info("calculator",".")
        print(result)
        self.assertAlmostEqual(result.startswith("- tests.py: "),True)
    
    def testCalcWithPkgDir(self):
        result = get_files_info("calculator","pkg")
        print(result)
        self.assertEqual(result.startswith("- "),True)
    
    def testCalcWithBadPath(self):
        result = get_files_info("calculator","/bin")
        print(result)
        self.assertEqual(result.startswith("Error: "),True)
  
if __name__ == "__main__":
    unittest.main()