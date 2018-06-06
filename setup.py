from setuptools import setup

setup(
    name='HAP-python-SDS011',
    description='HAP-python Accessory for the SDS011 sensor.',
    author='Ivan Kalchev',
    version='0.9',
    url='https://github.com/ikalchev/HAP-python-SDS011',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
    ],
    license='Apache-2.0',
    packages=[
        'pyhap.accessories.SDS011',
    ],
    install_requires=[
        'HAP-python',
    ],
)
