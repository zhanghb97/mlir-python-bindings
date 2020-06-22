find_package(pybind11)
link_directories(${CMAKE_BINARY_DIR}/lib/)
pybind11_add_module(mlir PythonBindings.cpp)
add_dependencies(mlir MLIR)
target_link_libraries(mlir PRIVATE MLIR)
set_target_properties(mlir PROPERTIES 
  PREFIX "" OUTPUT_NAME "mlir" SUFFIX ".so")
