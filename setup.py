from setuptools import find_packages, setup

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="car_gear_analysis",
    version="0.0.1",
    description="Car-Gear Analysis",
    package_dir={"": "app/src"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown"
)