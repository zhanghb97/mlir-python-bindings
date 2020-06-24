import site
site.addsitedir('./')
import mlir

# Get operation from milr file.
mlir.registerAllDialects()
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_region.mlir", ctx, sourcemgr)
operation = module.getOperation()
region = operation.getRegion(0)
block = region.front()
test_operation = block.front()

# Test Operation::getName()
def test_getName():
  return operation.getName()

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

# Test Operation::getNumOperands()
def test_getNumOperands():
  return operation.getNumOperands()

# Test Operation::getNumRegions()
def test_getNumRegions():
  return operation.getNumRegions()

# Test Operation::getRegion(unsigned index)
def test_getRegion():
  return operation.getRegion(0)
