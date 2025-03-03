import sys, unittest

'''
This is useful when you need certain tests to only be carried out within a
particular scenario or environment. To achieve selective testing, you can use 
either skip decorators (@unittest.skipIf, @unittest.skipUnless) or you can 
use the skipTest function!

- The skipUnless option skips the test if the condition evaluates to False.
- The skipIf option skips the test if the condition evaluates to True.

Signatures;
 - @unittest.skipIf(condition, message)
 - @unittest.skipUnless(condition, message)
 - self.skipTest('message')
'''

class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("linux") is False, "This test only runs on Linux")
    def test_linux_feature(self):
        print("This test should only run on Linux")

    @unittest.skipIf(sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("This test should only run on Linux2")

    def test_my_linux_feature(self):
        if not sys.platform.startswith("linux"):
            self.skipTest("Test only runs on Linux")


unittest.main()
