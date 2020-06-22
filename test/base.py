import unittest
import sys
sys.path.append('../../../build/lib/')
import mlir

import test_input
import test_module
import test_operation
import test_region
import test_block

class TestMLIR(unittest.TestCase):

  def test_input(self):
    self.assertIsInstance(test_input.test_constructor(), mlir.Module)

  def test_module(self):
    self.assertIsInstance(test_module.test_constructor(), mlir.Module)
    expect_list = ['module', 'module']
    result_list = test_module.test_getOperation()
    for r, e in result_list, expect_list:
      self.assertEqual(r, e)

  def test_operation(self):
    self.assertEqual(test_operation.test_getName(), 'module')
    self.assertIsInstance(test_operation.test_getRegion(), mlir.Region)

  def test_region(self):
    self.assertIsInstance(test_region.test_front(), mlir.Block)
    self.assertIsInstance(test_region.test_back(), mlir.Block)
    self.assertEqual(test_region.test_getParentOp(), 'module')

  def test_block(self):
    self.assertIsInstance(test_block.test_getParent(), mlir.Region)
    self.assertIsInstance(test_block.test_getParentOp(), mlir.Operation)
    self.assertFalse(test_block.test_isEntryBlock())
    self.assertFalse(test_block.test_args_empty())
    self.assertEqual(test_block.test_getNumArguments(), 2)
    self.assertIsInstance(test_block.test_front(), mlir.Operation)
    self.assertIsInstance(test_block.test_back(), mlir.Operation)

if __name__ == '__main__':
    unittest.main()

