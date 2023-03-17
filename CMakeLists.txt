################################################################################
##
## The University of Illinois/NCSA
## Open Source License (NCSA)
##
## Copyright (c) 2014-2021, Advanced Micro Devices, Inc. All rights reserved.
##
## Developed by:
##
##                 AMD Research and AMD HSA Software Development
##
##                 Advanced Micro Devices, Inc.
##
##                 www.amd.com
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to
## deal with the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:
##
##  - Redistributions of source code must retain the above copyright notice,
##    this list of conditions and the following disclaimers.
##  - Redistributions in binary form must reproduce the above copyright
##    notice, this list of conditions and the following disclaimers in
##    the documentation and/or other materials provided with the distribution.
##  - Neither the names of Advanced Micro Devices, Inc,
##    nor the names of its contributors may be used to endorse or promote
##    products derived from this Software without specific prior written
##    permission.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
## THE CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
## OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
## ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS WITH THE SOFTWARE.
##
################################################################################
cmake_minimum_required ( VERSION 3.7 )

## Clear target dependency data.
## Needed to allow UI transitions between static and dynamic builds.
## Need an update to CMake 3.12 to remove this hack. See CMake policy change
## CMP0073.
unset ( hsa-runtime64_LIB_DEPENDS CACHE )

## Set core runtime module name and project name.
set ( CORE_RUNTIME_NAME "hsa-runtime64" )
set ( CORE_RUNTIME_TARGET "${CORE_RUNTIME_NAME}" )
set ( CORE_RUNTIME_LIBRARY "lib${CORE_RUNTIME_TARGET}" )

## Set project name
project( ${CORE_RUNTIME_TARGET} )

add_subdirectory(src)

set(
    CMAKE_MODULE_PATH
        "${CMAKE_CURRENT_SOURCE_DIR}/tools/cmake" ${CMAKE_MODULE_PATH})
add_subdirectory(docs)