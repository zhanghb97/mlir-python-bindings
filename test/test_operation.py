import sys
sys.path.append('../../../build/lib/')
import mlir

# Get operation from milr file
mlir.registerAllDialects()
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_region.mlir", ctx, sourcemgr)
operation = module.getOperation()

# Test Operation::getName()
def test_getName():
  return operation.getName()

# Test Region::getRegion(unsigned index)
def test_getRegion():
  return operation.getRegion(0)
