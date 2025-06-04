import unittest
from unittest import result
from functions.get_files_info import get_file_content, get_files_info
from functions.write_files import overwrite_file
from functions.run_python import run_python_file


class TestGetFilesInfo(unittest.TestCase):
    # def testCalcWithCurrentDir(self):
    #     result = get_files_info("calculator",".")
    #     print(result)
    #     self.assertAlmostEqual(result.startswith("- "),True)
    
    # def testCalcWithPkgDir(self):
    #     result = get_files_info("calculator","pkg")
    #     print(result)
    #     self.assertEqual(result.startswith("- "),True)
    
    # def testCalcWithBadPath(self):
    #     result = get_files_info("calculator","/bin")
    #     print(result)
    #     self.assertEqual(result.startswith("Error: "),True)
    

    # def testReadFileCalc(self):
    #     result = get_file_content("calculator","pkg/calculator.py")
    #     print(result)
    #     self.assertEqual(type(result),str)
    
    # def testReadFileMain(self):
    #     result = get_file_content("calculator","main.py")
    #     print(result)
    #     self.assertEqual(type(result),str)

    
    # def testReadFileBadPath(self):
    #     result = get_file_content("calculator","/bin/cat")
    #     print(result)
    #     self.assertEqual(result.startswith("Error"),True)

    # def testOverWriteLorem(self):
    #     result = overwrite_file("calculator","lorem.txt","wait, this isn't lorem ipsum")
    #     print(result)
    #     self.assertEqual(type(result),str)

    # def testOverWriteNewFile(self):
    #     result = overwrite_file("calculator","pkg/morelorem.txt","lorem ipsum dolor sit amet")
    #     print(result)
    #     self.assertEqual(type(result),str)
    
    # def testOverWriteFileError(self):
    #     result = overwrite_file("calculator","/tmp/temp.txt","this should not be allowed")
    #     print(result)
    #     self.assertEqual(result.startswith("Error"),True)

    def testRunPythonFileCalculatorMain(self):
        results = run_python_file("calculator","main.py")
        print(results)
        self.assertEqual(type(results),str)
    def testRunPythonFileCalculatorTests(self):
        results = run_python_file("calculator","tests.py")
        print(results)
        self.assertEqual(type(results),str)
    def testRunPythonFileCalculatorBadDir(self):
        results = run_python_file("calculator","../main.py")
        print(results)
        self.assertEqual(results.startswith("Error:"),True)
    def testRunPythonFileCalculatorNoFile(self):
        results = run_python_file("calculator","empty.py")
        print(results)
        self.assertEqual(results.startswith("Error:"),True)
  
if __name__ == "__main__":
    unittest.main()