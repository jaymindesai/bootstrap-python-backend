import sys
import subprocess
import pkg_resources

from os import path
from setuptools import setup, find_packages
from setuptools import Command
from setuptools.command.test import test as TestCommand

here = path.abspath(path.dirname(__file__))


class PyTest(TestCommand):
    description = "Command to run all unit tests using PyTest"
    user_options = [('pytest-args', 'a', 'arguments to pass to pytest')]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = None
        self._test_target = 'tests/'

    def finalize_options(self):
        import shlex
        super().finalize_options()
        if self.pytest_args:
            self.pytest_args = shlex.split(self.pytest_args)
        else:
            self.pytest_args = ['--cov', 'app', self._test_target, '--cov-config', '.coveragerc']

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class BuildDocker(Command):
    description = "Command to build Docker image for current version"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        build_docker_script = path.join(here, "scripts", "build_docker_image.sh")
        command = ["bash", build_docker_script]
        subprocess.run(command)


with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

with open(path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    requirements = [str(req) for req in pkg_resources.parse_requirements(requirements_file.read())]

setup(
    name="backend-api",
    version=version,
    description='Flask API Server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jaymindesai/bootstrap-python-backend',
    packages=find_packages(exclude=['tests', 'docker']),
    install_requires=requirements,
    include_package_data=True,
    tests_require=['pytest', 'pytest-cov'],
    cmdclass=dict(test=PyTest, build_docker=BuildDocker),
)
