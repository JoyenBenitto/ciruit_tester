import os
import os.path
from arduino_tester.__init__ import __version__
from arduino_tester.__init__ import __author__
from arduino_tester.__init__ import __email__
import arduino_tester.generator as generator
import shutil
import click

build_dir = "./build"
os.system(f"rm -r {build_dir}")
os.system(f"mkdir {build_dir}")
generator.generate(build_dir)

# -------

# Top level group
@click.group()
@click.version_option(version=__version__)
def cli():
    ''' Command-line interface for arduino tester '''

@click.version_option(version=__version__)

@click.option(
    '--test_gen',
    '-t',
    help = 'This argument helps user to generate the test file',
    required = True
)

@click.option(
    '--show-table',
    is_flag = True,
    help = 'This flag enables the table display, gives the test summary to the user'
)


@click.option(
    '--build-dir',
    '-bd',
    help = 'This argument sets the directory where the output files are stored',
    default='./build',
    show_default = True,
    required = False
)

@cli.command()
def generate(test_gen ,build_dir ,show_table):
    '''Generating the .c test files'''
