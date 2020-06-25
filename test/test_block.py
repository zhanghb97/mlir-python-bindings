import site
site.addsitedir('./')
import mlir

# Get block from input file.
mlir.registerAllDialects()
ctx = mlir.Context()
sourcemgr = mlir.SourceMgr()
module = mlir.Module("./test_block.mlir", ctx, sourcemgr)
region = module.getOperation().getRegion(0)
block = region.front()
front_region = block.front().getRegion(0)

# Test Block::getParent()
def test_getParent():
  return block.getParent()

# Test Block::getParentOp()
def test_getParentOp():
  return block.getParentOp()

# Test Block::isEntryBlock()
def test_isEntryBlock():
  return front_region.back().isEntryBlock()

# Test Block::args_empty()
def test_args_empty():
  return front_region.back().args_empty()

def test_getNumArguments():
  return front_region.back().getNumArguments()

# Test Block::front()
def test_front():
  return block.front()

# Test Block::back()
def test_back():
  return block.back()

# Test Block::findAncestorOpInBlock(Operation &)
def test_findAncestorOpInBlock():
  operation = block.front()
  return block.findAncestorOpInBlock(operation)

# Test Block::isOpOrderValid()
def test_isOpOrderValid():
  return block.isOpOrderValid()

# Test Block::verifyOpOrder()
def test_verifyOpOrder():
  return block.verifyOpOrder()

# Test Block::getTerminator()
def test_getTerminator():
  return block.getTerminator()

# Test Block::hasNoPredecessors()
def test_hasNoPredecessors():
  return block.hasNoPredecessors()

# Test Block::getNumSuccessors()
def test_getNumSuccessors():
  return block.getNumSuccessors()
