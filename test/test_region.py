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

# Test Region::front()
def test_front():
  return region.front()

# Test Region::back()
def test_back():
  return region.back()

# Test Region::getParentOp()
def test_getParentOp():
  operation = region.getParentOp()
  return operation.getName()
