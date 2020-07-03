import sys
import os
sys.path.append(os.environ['MLIR_LIBRARY_PATH'])
import mlir

# Construct Module with context.
ctx = mlir.Context()
module = mlir.Module(ctx)
# Get operation twice to test ownership.
operation = module.getOperation()
name = operation.getName()
same_operation = module.getOperation()
same_name = same_operation.getName()

# Test Module constructor with MLIRContext
def test_constructor():
  return module

# Test Module::getOperation()
def test_getOperation():
  return_list = []
  return_list.append(name)
  return_list.append(same_name)
  return return_list
