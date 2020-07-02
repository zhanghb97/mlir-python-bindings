import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
import mlir

# Test Module constructor with mlir file.
def test_constructor():
  mlir.registerAllDialects()
  ctx = mlir.Context()
  sourcemgr = mlir.SourceMgr()
  module = mlir.Module("./test_input.mlir", ctx, sourcemgr)
  return module
