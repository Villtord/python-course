cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

#add_subdirectory(pybind11)
pybind11_add_module(cmake_example src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(cmake_example
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
