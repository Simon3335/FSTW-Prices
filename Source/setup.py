# Important:  please note that some unesseary packages were manually modified
# or removed to reduce space.  The size generated by this setup script will be
# larger than that of the distribution package

import os

from cx_Freeze import setup, Executable

path = os.getcwd()

buildOptions = dict(
    packages = [],
    excludes = [
        'asyncio',
        'xml',
        'xmlrpc',
        '_ssl',
        '_socket',
        'lzma',
        'hashlib',
        'bz2',
        'urllib',
        'unittest',
        'pydoc_data',
        'logging',
        'http',
        'html',
        'email',
    ],
    include_files = [
        "C:\\Users\\Nicholas\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tcl86t.dll",
        "C:\\Users\\Nicholas\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tk86t.dll",
        "C:\\Users\\Nicholas\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tcl8.6",
        "C:\\Users\\Nicholas\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tk8.6",
        "icon.ico",
        os.path.join(path, "FSTW_prices.json"),
        os.path.join(path, "license.txt")       
    ]
)

executables = [
    Executable(
        script="main.py",
        base="Win32GUI",
        icon="icon.ico"

    )
]

setup(
    name="FSTW Prices",
    version = "1.0",
    description = "Fortnite Save The World calcualtor, for calculating a fair price for materials, quickly, and easily!",
    options = dict(build_exe = buildOptions),
    executables = executables
)
