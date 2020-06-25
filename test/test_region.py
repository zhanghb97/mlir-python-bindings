import site
site.addsitedir('./')
import mlir

# Get region
mlir.registerAllDialects()
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_region.mlir", ctx, sourcemgr)
operation = module.getOperation()
region = operation.getRegion(0)
block = region.front()
front_region = block.front().getRegion(0)

# Test Region::empty()
def test_empty():
  return region.empty()

# Test Region::front()
def test_front():
  return region.front()

# Test Region::back()
def test_back():
  return region.back()

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
