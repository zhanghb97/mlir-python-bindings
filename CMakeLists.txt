find_package(pybind11)
link_directories(${CMAKE_BINARY_DIR}/lib/)
pybind11_add_module(mlir PythonBindings.cpp)
target_link_libraries(mlir PRIVATE libMLIR.so)
set_target_properties(mlir PROPERTIES 
  PREFIX "" OUTPUT_NAME "mlir" SUFFIX ".so"
  LIBRARY_OUTPUT_DIRECTORY ${MLIR_MAIN_SRC_DIR}/bindings/test)
