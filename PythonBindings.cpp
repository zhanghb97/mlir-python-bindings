//===- PythonBindings.cpp - MLIR Python Bindings -===//
//
// Part of Google Summer of Code 2020 Project.
//
//===---------------------------------------------===//
//
// This file defines MLIR Python bindings 
// and corresponding classes and functions.
//
//===---------------------------------------------===//

#include <string>
#include <pybind11/pybind11.h>
#include "mlir/IR/Module.h"

namespace mlir {
namespace python {
namespace py = pybind11;

/// PythonModule class contains module member.
/// It can dump the module content and
/// get the operation pointer of the module.
class PythonModule {
public:
  PythonModule(MLIRContext &context) {
    module = ModuleOp::create(UnknownLoc::get(&context));
  }

  void dump() {
    module->dump();
  }

  Operation *getOperation() {
    ModuleOp moduleOp = module.get();
    Operation *operation = moduleOp.getOperation();
    return operation;
  }

  OwningModuleRef module;
};

/// Get the name of an operation.
std::string getOperationName(Operation *operation) {
  OperationName operationName = operation->getName();
  llvm::StringRef name = operationName.getStringRef();
  return name.str();
}

/// Python bindings with pybind11.
PYBIND11_MODULE(mlir, m) {
  m.doc() =
    "Python bindings for MLIR";

  py::class_<MLIRContext>(
    m, "Context", "MLIR Context")
    .def(py::init<>());

  py::class_<PythonModule>(
    m, "Module", "MLIR Module")
    .def(py::init<MLIRContext&>(), py::keep_alive<1, 2>())
    .def("dump", &PythonModule::dump)
    .def("getOperation", &PythonModule::getOperation);

  py::class_<mlir::Operation, std::unique_ptr<mlir::Operation, py::nodelete>>(
    m, "Operation", "MLIR Operation")
    .def("getName", &getOperationName);
}

}  // namespace python
}  // namespace mlir
