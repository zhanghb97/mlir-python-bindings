find_package(pybind11)
link_directories(${CMAKE_BINARY_DIR}/lib/)
pybind11_add_module(mlir PythonBindings.cpp)
add_dependencies(mlir MLIR)
target_link_libraries(mlir PRIVATE MLIR)
set(MLIR_LIBRARY_PATH "${CMAKE_BINARY_DIR}/lib/"
  CACHE PATH "Default MLIR library path")
set_target_properties(mlir PROPERTIES 
  PREFIX "" OUTPUT_NAME "mlir" SUFFIX ".so"
  LIBRARY_OUTPUT_DIRECTORY ${MLIR_LIBRARY_PATH})
file(WRITE ./test/mlir.pth ${MLIR_LIBRARY_PATH})
