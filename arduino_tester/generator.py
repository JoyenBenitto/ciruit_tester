import os
import arduino_tester.template as template 

def generate(build_dir):

    defines = ""
    pin_mode_arduino1= ""
    pin_mode_arduino2= ""

    for pin in range(15):
        defines += f"#define D{pin} {pin}\n".format(pin)
        pin_mode_arduino1 += template.template_pinmode.format(
            pin_number = f'D{pin}',
            in_out = f'OUTPUT'
        )
        pin_mode_arduino2 += template.template_pinmode.format(
            pin_number = f'D{pin}',
            in_out = f'INPUT'
        ) 

    frame_arduino1 = template.template_frame.format(
        defines = defines,
        pin_mode = pin_mode_arduino1,
        t = "{",
        p = "}",
        logic = ""
    )

    frame_arduino2 = template.template_frame.format(
        defines = defines,
        pin_mode = pin_mode_arduino2,
        t = "{",
        p = "}",
        logic = ""
    )

    with open(f"{build_dir}/test1.c", "a") as fp:
        fp.write(frame_arduino1)
    with open(f"{build_dir}/test2.c", "a") as fp:
        fp.write(frame_arduino2)