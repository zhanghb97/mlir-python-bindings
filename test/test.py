import mlir

# Initial the context and module.
ctx = mlir.Context()
module = mlir.Module(ctx)
# Get operation from module.
operation = module.getOperation()
# Get and print operation name.
name = mlir.getOperationName(operation)
print(name)
# Get same operation from module.
same_operation = module.getOperation()
# Get and print same operation name.
same_name = mlir.getOperationName(same_operation)
print(same_name)
