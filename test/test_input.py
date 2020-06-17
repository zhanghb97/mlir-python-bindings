import mlir

# Register all dialects.
mlir.registerAllDialects()
# Initial the Context and SourceMgr.
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
# Get module from input file.
module = mlir.Module("./test.mlir", ctx, sourcemgr)
# Get operation from module.
operation = module.getOperation()
# Get and print operation name.
name = operation.getName()
print(name)
# Dump the module
module.dump()
