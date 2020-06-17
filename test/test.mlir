llvm.func @main() -> !llvm.float {
  %0 = llvm.mlir.constant(-4.200000e+02 : f32) : !llvm.float
  llvm.return %0 : !llvm.float
}
