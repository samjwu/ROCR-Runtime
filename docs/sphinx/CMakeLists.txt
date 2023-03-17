set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/source)
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR})

add_custom_target(
    sphinx_docs ALL
    COMMAND ${SPHINX_EXECUTABLE} -b html ${SPHINX_SOURCE} ${SPHINX_BUILD}
    -Dbreathe_projects.hsa-runtime64=${CMAKE_CURRENT_BINARY_DIR}/../doxygen/xml
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/..)