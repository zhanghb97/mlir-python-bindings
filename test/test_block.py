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
# Get region from operation.
region = operation.getRegion(0)
# Get block from region.
block = region.front()
# Test Block::getParent()
parent_region = block.getParent()
print(parent_region)
# Test Block::getOperationOp()
parent_operation = block.getParentOp()
print(parent_operation.getName())
# Test Block::front()
block_operation = block.front()
print(block_operation.getName())
# Get region from operation.
block_region = block_operation.getRegion(0)
# Get block from region
blk = block_region.back()
# Test Block::dump()
blk.dump()
# Test Block::isEntryBlock()
print(blk.isEntryBlock())
# Test Block::args_empty()
print(blk.args_empty())
# Test Block::getNumArguments()
print(blk.getNumArguments())
