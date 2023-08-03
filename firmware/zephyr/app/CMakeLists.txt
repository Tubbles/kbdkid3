# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.25.1)

list(APPEND BOARD_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(peripheral_hids)

set(app_sources
    src/main.c
    src/hog.c
)

target_sources(app PRIVATE
    ${app_sources}
)
