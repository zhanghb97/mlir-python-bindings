import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
import mlir

# Get region from milr file.
mlir.registerAllDialects()
ctx = mlir.Context()
ctx.allowUnregisteredDialects(True)
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_region.mlir", ctx, sourcemgr)
operation = module.getOperation()
region = operation.getRegion(0)
block = region.front()
front_region = block.front().getRegion(0)

# Test Region::getContext()
def test_getContext():
  return region.getContext()

# Test Region::getParentRegion()
def test_getParentRegion():
  return front_region.getParentRegion()

# Test Region::getParentOp()
def test_getParentOp():
  operation = region.getParentOp()
  return operation.getName()

# Test Region::getRegionNumber()
def test_getRegionNumber():
  return region.getRegionNumber()

# Test Region::isProperAncestor(Region *)
def test_isProperAncestor():
  return_list = []
  return_list.append(region.isProperAncestor(region))
  return_list.append(region.isProperAncestor(front_region))
  return return_list

# Test Region::isAncestor(Region *)
def test_isAncestor():
  return_list = []
  return_list.append(region.isAncestor(region))
  return_list.append(region.isAncestor(front_region))
  return return_list

# Test Region::findAncestorBlockInRegion(Block &)
def test_findAncestorBlockInRegion():
  return region.findAncestorBlockInRegion(block)

# Test Region iterator.
def test_iterator():
  return [test_block for test_block in front_region]

# Test Region reversed iterator.
def test_iterator_reversed():
  return [test_block for test_block in reversed(front_region)]

# Test Region::empty()
def test_empty():
  return region.empty()

# Test Region::back()
def test_back():
  return region.back()

# Test Region::front()
def test_front():
  return region.front()
