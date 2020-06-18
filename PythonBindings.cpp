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
#include "mlir/InitAllDialects.h"
#include "mlir/Parser.h"
#include "mlir/Support/FileUtilities.h"
#include "llvm/Support/SourceMgr.h"

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

  PythonModule(std::string mlirFileName, 
               MLIRContext &context, llvm::SourceMgr &sourceMgr) {
    // Set up the error message.
    std::string errorMessage;
    // Set up the input file.
    auto file = openInputFile(mlirFileName, &errorMessage);
    if (!file) {
      llvm::errs() << errorMessage << "\n";
    }
    // Parse the input file.
    sourceMgr.AddNewSourceBuffer(std::move(file), llvm::SMLoc());
    module = parseSourceFile(sourceMgr, &context);
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

  py::class_<llvm::SourceMgr>(
    m, "SourceMgr", "MLIR SourceMgr")
    .def(py::init<>());

  py::class_<PythonModule>(
    m, "Module", "MLIR Module")
    .def(py::init<MLIRContext&>(), py::keep_alive<1, 2>())
    .def(py::init<std::string, MLIRContext&, llvm::SourceMgr&>(), 
         py::keep_alive<1, 2>())
    .def("dump", &PythonModule::dump)
    .def("getOperation", &PythonModule::getOperation);

  py::class_<mlir::Operation, std::unique_ptr<mlir::Operation, py::nodelete>>(
    m, "Operation", "MLIR Operation")
    .def("getName", &getOperationName);

  m.def("registerAllDialects", 
        static_cast<void (&)()>(registerAllDialects), "Register all dialects");
}

}  // namespace python
}  // namespace mlir
