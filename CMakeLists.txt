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

add_custom_target(check-mlir-python
  COMMAND ${CMAKE_COMMAND} -E env
          MLIR_LIBRARY_PATH=${MLIR_LIBRARY_PATH}
          "${Python3_EXECUTABLE}" -B -m unittest base -v
  DEPENDS mlir
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/test)
