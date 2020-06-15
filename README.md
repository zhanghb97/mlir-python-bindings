# MLIR Python Bindings
MLIR Python Bindings is a project of Google Summer of Code 2020.

## Getting the Source Code and Building Python Bindings

This is the work-flow and configuration to get and build MLIR Python Bindings:

1. Clone llvm-project (The MLIR Python Bindings project is based on the LLVM system. ):
   - `git clone git@github.com:llvm/llvm-project.git`

   Clone the mlir-python-bindings in the specific directory:

   - `cd llvm-project/mlir`

   - `git clone git@github.com:zhanghb97/mlir-python-bindings.git bindings`

2. Configure and build MLIR and mlir-python-bindings:

   - `cd llvm-project`

   - `mkdir build`

   - `cd build`

   - Configure the project:

     ```text
     cmake -G Ninja ../llvm \
       -DLLVM_ENABLE_PROJECTS=mlir\
       -DLLVM_TARGETS_TO_BUILD="host"\
       -DCMAKE_BUILD_TYPE=Release\
       -DLLVM_BUILD_LLVM_DYLIB=ON\
       -DLLVM_LINK_LLVM_DYLIB=ON
     ```

   - `cmake --build .`

3. Test the shared library:

   - `cd llvm-project/mlir/bindings/test`
   - `python test.py`

