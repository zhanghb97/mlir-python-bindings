import mlir

# Initial the context and module.
ctx = mlir.Context()
module = mlir.Module(ctx)
# Get operation from module.
operation = module.getOperation()
# Get and print operation name.
name = operation.getName()
print(name)
# Get same operation from module.
same_operation = module.getOperation()
# Get and print same operation name.
same_name = same_operation.getName()
print(same_name)
