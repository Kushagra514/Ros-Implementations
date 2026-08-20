# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mini_radi_gazebo_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mini_radi_gazebo_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mini_radi_gazebo_FOUND FALSE)
  elseif(NOT mini_radi_gazebo_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mini_radi_gazebo_FOUND FALSE)
  endif()
  return()
endif()
set(_mini_radi_gazebo_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mini_radi_gazebo_FIND_QUIETLY)
  message(STATUS "Found mini_radi_gazebo: 0.0.0 (${mini_radi_gazebo_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mini_radi_gazebo' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mini_radi_gazebo_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mini_radi_gazebo_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mini_radi_gazebo_DIR}/${_extra}")
endforeach()
