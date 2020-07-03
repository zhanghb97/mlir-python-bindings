import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
import mlir

# Get block from input file.
mlir.registerAllDialects()
ctx = mlir.Context()
ctx.allowUnregisteredDialects(True)
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_block.mlir", ctx, sourcemgr)
region = module.getOperation().getRegion(0)
block = region.front()
front_region = block.front().getRegion(0)

# Test Block::getParent()
def test_getParent():
  return block.getParent()

# Test Block::getParentOp()
def test_getParentOp():
  return block.getParentOp()

# Test Block::isEntryBlock()
def test_isEntryBlock():
  return front_region.back().isEntryBlock()

# Test Block::args_empty()
def test_args_empty():
  return front_region.back().args_empty()

def test_getNumArguments():
  return front_region.back().getNumArguments()

# Test Block::findAncestorOpInBlock(Operation &)
def test_findAncestorOpInBlock():
  operation = block.front()
  return block.findAncestorOpInBlock(operation)

# Test Block::isOpOrderValid()
def test_isOpOrderValid():
  return block.isOpOrderValid()

# Test Block::verifyOpOrder()
def test_verifyOpOrder():
  return block.verifyOpOrder()

# Test Block::getTerminator()
def test_getTerminator():
  return block.getTerminator()

# Test Block::hasNoPredecessors()
def test_hasNoPredecessors():
  return block.hasNoPredecessors()

# Test Block::getSinglePredecessor()
def test_getSinglePredecessor():
  operation_list = [operation for operation in block]
  test_region = operation_list[2].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[2].getSinglePredecessor()

# Test Block::getUniquePredecessor()
def test_getUniquePredecessor():
  operation_list = [operation for operation in block]
  test_region = operation_list[2].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[2].getUniquePredecessor()

# Test Block::getNumSuccessors()
def test_getNumSuccessors():
  operation_list = [operation for operation in block]
  test_region = operation_list[2].getRegion(0)
  test_block_list = [block for block in test_region]
  return test_block_list[0].getNumSuccessors()

# Test Block::getSuccessor(unsigned)
def test_getSuccessor():
  operation_list = [operation for operation in block]
  test_region = operation_list[2].getRegion(0)
  test_block_list = [block for block in test_region]
  successor_num = test_block_list[0].getNumSuccessors()
  return_list = []
  for i in range(successor_num):
    return_list.append(test_block_list[0].getSuccessor(i))
  return return_list

# Test Block iterator
def test_iterator():
  return [operation for operation in block]

# Test Block reversed iterator.
def test_iterator_reversed():
  return [operation for operation in reversed(block)]

# Test Block::empty()
def test_empty():
  return block.empty()

# Test Block::front()
def test_front():
  return block.front()

# Test Block::back()
def test_back():
  return block.back()
