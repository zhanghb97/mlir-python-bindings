import mlir

# Register all dialects.
mlir.registerAllDialects()
# Initial the Context and SourceMgr.
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
# Get module from input file.
module = mlir.Module("./test_region.mlir", ctx, sourcemgr)
# Get operation from module.
operation = module.getOperation()
# Get region from operation
region = operation.getRegion(0)
# Test region.front()
block = region.front()
block.dump()
# Test region.getParentOp
parent_operation = region.getParentOp()
print(parent_operation.getName())