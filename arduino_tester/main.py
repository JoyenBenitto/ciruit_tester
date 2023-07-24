import os
import generator as generator

build_dir = "./build"
os.system(f"rm -r {build_dir}")
os.system(f"mkdir {build_dir}")
generator.generate(build_dir)