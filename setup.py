from setuptools import setup
from sysperf import __version__

setup(name="sysperf",
      version=__version__,
      description="System performance dashboard showing real time cpu, memory, swap, disk and network performance metrics",
      author="W.T.S. Warnapura - IT20084936 , R.H.M.I.D. Rajakaruna - IT20246396 ",
      packages=["sysperf"],
      author_email="IT20246396@my.sliit.lk, IT20084936@my.sliit.lk",
      url="https://github.com/ImeshDilshan/System-Performance-Risk-Assessment-Dashboard.git",
      install_requires=[
            'Flask',
            'psutil'
      ],
      include_package_data=True,
      entry_points={
              'console_scripts': [
                  'sysperf = sysperf.perf'
              ]
            }
      )
