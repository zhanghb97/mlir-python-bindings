//===- PythonBindings.cpp - MLIR Python Bindings --------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This file implements MLIR Python bindings.
//
//===----------------------------------------------------------------------===//

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
    .def(py::init<>())
    .def("allowUnregisteredDialects", &MLIRContext::allowUnregisteredDialects);

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

  py::class_<Operation, std::unique_ptr<Operation, py::nodelete>>(
    m, "Operation", "MLIR Operation")
    .def("getName", &getOperationName)
    .def("isRegistered", &Operation::isRegistered)
    .def("getBlock", &Operation::getBlock)
    .def("getContext", &Operation::getContext)
    .def("getParentRegion", &Operation::getParentRegion)
    .def("getParentOp", &Operation::getParentOp)
    .def("isProperAncestor", &Operation::isProperAncestor)
    .def("isAncestor", &Operation::isAncestor)
    .def("isBeforeInBlock", &Operation::isBeforeInBlock)
    .def("dump", &Operation::dump)
    .def("getNumOperands", &Operation::getNumOperands)
    .def("getNumRegions", &Operation::getNumRegions)
    .def("getRegion", &Operation::getRegion, py::return_value_policy::reference)
    .def("hasSuccessors", &Operation::hasSuccessors)
    .def("getNumSuccessors", &Operation::getNumSuccessors)
    .def("isCommutative", &Operation::isCommutative)
    .def("isKnownTerminator", &Operation::isKnownTerminator)
    .def("isKnownNonTerminator", &Operation::isKnownNonTerminator)
    .def("isKnownIsolatedFromAbove", &Operation::isKnownIsolatedFromAbove)
    .def("hasOneUse", &Operation::hasOneUse)
    .def("use_empty", &Operation::use_empty)
    .def("isUsedOutsideOfBlock", &Operation::isUsedOutsideOfBlock);

  py::class_<Region>(m, "Region", "MLIR Region")
    .def(py::init<>())
    .def("getContext", &Region::getContext)
    .def("getParentRegion", &Region::getParentRegion)
    .def("getParentOp", &Region::getParentOp)
    .def("getRegionNumber", &Region::getRegionNumber)
    .def("isProperAncestor", &Region::isProperAncestor)
    .def("isAncestor", &Region::isAncestor)
    .def("findAncestorBlockInRegion", &Region::findAncestorBlockInRegion)
    // Iteration over the blocks in the region.
    .def("__iter__", [](Region *region) {
      return py::make_iterator(region->begin(), region->end());
    }, py::keep_alive<0, 1>())
    .def("__reversed__", [](Region *region) {
      return py::make_iterator(region->rbegin(), region->rend());
    }, py::keep_alive<0, 1>())
    .def("empty", &Region::empty)
    .def("back", &Region::back, py::return_value_policy::reference)
    .def("front", &Region::front, py::return_value_policy::reference);
  
  py::class_<Block>(m, "Block", "MLIR Block")
    .def(py::init<>())
    .def("getParent", &Block::getParent)
    .def("getParentOp", &Block::getParentOp)
    .def("isEntryBlock", &Block::isEntryBlock)
    .def("args_empty", &Block::args_empty)
    .def("getNumArguments", &Block::getNumArguments)
    .def("findAncestorOpInBlock", &Block::findAncestorOpInBlock)
    .def("isOpOrderValid", &Block::isOpOrderValid)
    .def("verifyOpOrder", &Block::verifyOpOrder)
    .def("getTerminator", &Block::getTerminator)
    .def("hasNoPredecessors", &Block::hasNoPredecessors)
    .def("getSinglePredecessor", &Block::getSinglePredecessor)
    .def("getUniquePredecessor", &Block::getUniquePredecessor)
    .def("getNumSuccessors", &Block::getNumSuccessors)
    .def("getSuccessor", &Block::getSuccessor)
    .def("dump", &Block::dump)
    // Iteration over the operations in the block.
    .def("__iter__", [](Block *block) {
      return py::make_iterator(block->begin(), block->end());
    }, py::keep_alive<0, 1>())
    .def("__reversed__", [](Block *block) {
      return py::make_iterator(block->rbegin(), block->rend());
    }, py::keep_alive<0, 1>())
    .def("empty", &Block::empty)
    .def("back", &Block::back, py::return_value_policy::reference)
    .def("front", &Block::front, py::return_value_policy::reference);;
  
  m.def("registerAllDialects", 
        static_cast<void (&)()>(registerAllDialects), "Register all dialects");
}

}  // namespace python
}  // namespace mlir
