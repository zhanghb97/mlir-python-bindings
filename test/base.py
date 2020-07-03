import unittest
import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
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
    self.assertListEqual(expect_list, result_list)

  def test_operation(self):
    self.assertEqual(test_operation.test_getName(), 'module')
    self.assertTrue(test_operation.test_isRegistered())
    self.assertIsInstance(test_operation.test_getBlock(), mlir.Block)
    self.assertIsInstance(test_operation.test_getContext(), mlir.Context)
    self.assertIsInstance(test_operation.test_getParentRegion(), mlir.Region)
    self.assertIsInstance(test_operation.test_getParentOp(), mlir.Operation)
    isProperAncestor_expect_list = [False, True]
    isProperAncestor_return_list = test_operation.test_isProperAncestor()
    self.assertListEqual(isProperAncestor_expect_list,
                         isProperAncestor_return_list)
    isAncestor_expect_list = [True, True]
    isAncestor_return_list = test_operation.test_isAncestor()
    self.assertListEqual(isAncestor_expect_list, isAncestor_return_list)
    self.assertTrue(test_operation.test_isBeforeInBlock())
    self.assertEqual(test_operation.test_getNumOperands(), 0)
    self.assertEqual(test_operation.test_getNumRegions(), 1)
    self.assertIsInstance(test_operation.test_getRegion(), mlir.Region)
    self.assertTrue(test_operation.test_hasSuccessors())
    self.assertEqual(test_operation.test_getNumSuccessors(), 2)
    self.assertFalse(test_operation.test_isCommutative())
    self.assertTrue(test_operation.test_isKnownTerminator())
    self.assertTrue(test_operation.test_isKnownNonTerminator())
    self.assertTrue(test_operation.test_isKnownIsolatedFromAbove())
    self.assertTrue(test_operation.test_hasOneUse())
    self.assertTrue(test_operation.test_use_empty())
    self.assertTrue(test_operation.test_isUsedOutsideOfBlock())

  def test_region(self):
    self.assertIsInstance(test_region.test_getContext(), mlir.Context)
    self.assertFalse(test_region.test_empty())
    self.assertIsInstance(test_region.test_front(), mlir.Block)
    self.assertIsInstance(test_region.test_back(), mlir.Block)
    self.assertIsInstance(test_region.test_getParentRegion(), mlir.Region)
    self.assertEqual(test_region.test_getParentOp(), 'module')
    self.assertEqual(test_region.test_getRegionNumber(), 0)
    isProperAncestor_expect_list = [False, True]
    isProperAncestor_return_list = test_region.test_isProperAncestor()
    self.assertListEqual(isProperAncestor_expect_list,
                         isProperAncestor_return_list)
    isAncestor_expect_list = [True, True]
    isAncestor_return_list = test_region.test_isAncestor()
    self.assertListEqual(isAncestor_expect_list, isAncestor_return_list)
    self.assertIsInstance(test_region.test_findAncestorBlockInRegion(), mlir.Block)
    iterator_return_list = test_region.test_iterator()
    for it in iterator_return_list:
      self.assertIsInstance(it, mlir.Block)
    iterator_reversed_list = test_region.test_iterator_reversed()
    for it in iterator_reversed_list:
      self.assertIsInstance(it, mlir.Block)

  def test_block(self):
    self.assertIsInstance(test_block.test_getParent(), mlir.Region)
    self.assertIsInstance(test_block.test_getParentOp(), mlir.Operation)
    self.assertTrue(test_block.test_isEntryBlock())
    self.assertTrue(test_block.test_args_empty())
    self.assertEqual(test_block.test_getNumArguments(), 0)
    self.assertIsInstance(test_block.test_findAncestorOpInBlock(), mlir.Operation)
    self.assertFalse(test_block.test_isOpOrderValid())
    self.assertFalse(test_block.test_verifyOpOrder())
    self.assertIsInstance(test_block.test_getTerminator(), mlir.Operation)
    self.assertEqual(test_block.test_getTerminator().getName(), 'module_terminator')
    self.assertTrue(test_block.test_hasNoPredecessors())
    self.assertIsInstance(test_block.test_getSinglePredecessor(), mlir.Block)
    self.assertIsInstance(test_block.test_getUniquePredecessor(), mlir.Block)
    self.assertEqual(test_block.test_getNumSuccessors(), 2)
    successor_return_list = test_block.test_getSuccessor()
    for successor in successor_return_list:
      self.assertIsInstance(successor, mlir.Block)
    iterator_return_list = test_block.test_iterator()
    for it in iterator_return_list:
      self.assertIsInstance(it, mlir.Operation)
    iterator_reversed_list = test_block.test_iterator_reversed()
    for it in iterator_reversed_list:
      self.assertIsInstance(it, mlir.Operation)
    self.assertFalse(test_block.test_empty())
    self.assertIsInstance(test_block.test_back(), mlir.Operation)
    self.assertIsInstance(test_block.test_front(), mlir.Operation)

if __name__ == '__main__':
  unittest.main()
