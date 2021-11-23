#!/bin/bash

cd ~/Modules
sudo insmod fpga_interface_driver.ko

sudo insmod fpga_led_driver.ko
sudo mknod /dev/fpga_led c 260 0

sudo insmod fpga_fnd_driver.ko
sudo mknod /dev/fpga_fnd c 261 0

sudo insmod fpga_dot_driver.ko
sudo mknod /dev/fpga_dot c 262 0

sudo insmod fpga_text_lcd_driver.ko
sudo mknod /dev/fpga_text_lcd c 263 0

sudo insmod fpga_dip_switch_driver.ko
sudo mknod /dev/fpga_dip_switch c 266 0

sudo insmod fpga_push_switch_driver.ko
sudo mknod /dev/fpga_push_switch c 265 0

sudo insmod fpga_step_motor_driver.ko
sudo mknod /dev/fpga_step_motor c 267 0
