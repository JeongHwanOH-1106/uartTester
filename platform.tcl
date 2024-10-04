# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\MOA\vitis_workspace\SSAS_FC_TOP\SSAS_FC_TOP_Safe_v0_0_0_20240920\SSAS_FC_BSP_20240920\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\MOA\vitis_workspace\SSAS_FC_TOP\SSAS_FC_TOP_Safe_v0_0_0_20240920\SSAS_FC_BSP_20240920\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {SSAS_FC_BSP_20240920}\
-hw {C:\Users\MOA\vitis_workspace\SSAS_FC_TOP\project_3_24.03.21_gpio (2)\TOP.xsa}\
-proc {ps7_cortexa9_0} -os {standalone} -out {C:/Users/MOA/vitis_workspace/SSAS_FC_TOP/SSAS_FC_TOP_Safe_v0_0_0_20240920}

platform write
platform generate -domains 
platform active {SSAS_FC_BSP_20240920}
platform generate
bsp reload
bsp setlib -name lwip211 -ver 1.8
bsp setlib -name xilffs -ver 4.8
bsp config clocking "true"
bsp config hypervisor_guest "true"
bsp config xil_interrupt "true"
bsp config enable_exfat "true"
bsp config fs_interface "1"
bsp config enable_multi_partition "true"
bsp config use_chmod "true"
bsp config use_trim "true"
bsp write
bsp reload
catch {bsp regenerate}
platform generate -domains standalone_domain 
catch {platform remove SSAS_FC_BSP_20240911}
platform clean
platform generate
