import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
import mlir

# Get operation from milr file.
mlir.registerAllDialects()
ctx = mlir.Context()
ctx.allowUnregisteredDialects(True)
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_operation.mlir", ctx, sourcemgr)
operation = module.getOperation()
region = operation.getRegion(0)
block = region.front()
test_operation = block.front()

# Test Operation::getName()
def test_getName():
  return operation.getName()

# Test Operation::isRegistered()
def test_isRegistered():
  return operation.isRegistered()

# Test Operation::getBlock()
def test_getBlock():
  return test_operation.getBlock()

# Test Operation::getContext()
def test_getContext():
  return operation.getContext()

# Test Operation::getParentRegion()
def test_getParentRegion():
  return test_operation.getParentRegion()

# Test Operation::getParentOp()
def test_getParentOp():
  return test_operation.getParentOp()

# Test Operation::isProperAncestor(Operation *)
def test_isProperAncestor():
  return_list = []
  return_list.append(operation.isProperAncestor(operation))
  return_list.append(operation.isProperAncestor(test_operation))
  return return_list

# Test Operation::isAncestor(Operation *)
def test_isAncestor():
  return_list = []
  return_list.append(operation.isAncestor(operation))
  return_list.append(operation.isAncestor(test_operation))
  return return_list

# Test Operation::isBeforeInBlock(Operation *)
def test_isBeforeInBlock():
  test_operation = block.front()
  other_operation = block.back()
  return test_operation.isBeforeInBlock(other_operation)

# Test Operation::getNumOperands()
def test_getNumOperands():
  return operation.getNumOperands()

# Test Operation::getNumRegions()
def test_getNumRegions():
  return operation.getNumRegions()

# Test Operation::getRegion(unsigned index)
def test_getRegion():
  return operation.getRegion(0)

# Test Operation::hasSuccessors()
def test_hasSuccessors():
  operation_list = [operation for operation in block]
  test_region = operation_list[1].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[0].front().hasSuccessors()

# Test Operation::getNumSuccessors()
def test_getNumSuccessors():
  operation_list = [operation for operation in block]
  test_region = operation_list[1].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[0].front().getNumSuccessors()

# Test Operation::isCommutative()
def test_isCommutative():
  return operation.isCommutative()

# Test Operation::isKnownTerminator()
def test_isKnownTerminator():
  return block.back().isKnownTerminator()

# Test Operation::isKnownNonTerminator()
def test_isKnownNonTerminator():
  return block.front().isKnownNonTerminator()

# Test Operation::isKnownIsolatedFromAbove()
def test_isKnownIsolatedFromAbove():
  return operation.isKnownIsolatedFromAbove()

# Test Operation::hasOneUse()
def test_hasOneUse():
  operation_list = [operation for operation in block]
  test_region = operation_list[1].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[5].front().hasOneUse()

# Test Operation::use_empty()
def test_use_empty():
  return operation.use_empty()

# Test Operation::isUsedOutsideOfBlock(Block *)
def test_isUsedOutsideOfBlock():
  operation_list = [operation for operation in block]
  test_region = operation_list[1].getRegion(0)
  test_block_list = [block for block in test_region]
  test_operation = test_block_list[2].front()
  test_block = test_block_list[2]
  return test_operation.isUsedOutsideOfBlock(test_block)
