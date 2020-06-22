import sys
sys.path.append('../../../build/lib/')
import mlir

# Test Module constructor with mlir file.
def test_constructor():
  mlir.registerAllDialects()
  ctx = mlir.Context()
  sourcemgr = mlir.SourceMgr()
  module = mlir.Module("./test_input.mlir", ctx, sourcemgr)
  return module
