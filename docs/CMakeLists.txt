find_package(Doxygen)

if (Doxygen_FOUND)
    add_subdirectory(doxygen)

    find_package(Sphinx)
    if (Sphinx_FOUND)
        add_subdirectory(sphinx)
    endif ()
endif ()