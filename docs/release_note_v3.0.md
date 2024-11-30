|     Font      |     Back      |
| ------------- | ------------- |
|![PCB Top design](https://github.com/<<repo_name>>/releases/download/<<tag>>/<<ID>>_<<project_name>>_<<version>>_PCBdraw_Top.png)|![PCB Back design](https://github.com/<<repo_name>>/releases/download/<<tag>>/<<ID>>_<<project_name>>_<<version>>_PCBdraw_Back.png)|

first RC release

New
* Added ATtiny1616 in QFN package as an option
* Added MOSFETS for the LEDs 
* Added programming capacitor for the CP2105 (see #4)
* Added Test Points 

Changes
* use PA4 / PA5 for the LEDs as this pins have PWM (see #2)
* decouple CP2105 from direct VBUS and use the DPDT switch (see #5)
* Footprint for the DPDT to habe a secound source option
* more information for BOM and components


Breaking Changes
* removed jumper for LEDs
* stencil fom v2.0 mostly not compatible 

