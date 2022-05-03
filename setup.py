from setuptools import find_packages, setup


setup(
    name='requests-walmart-auth',
    version='1.0.0',
    description='python requests support for the Walmart Affiliate Marketplace (REST) API required Additional Headers',
    url='https://github.com/Terrabits/requests-walmart-auth',
    author='Nick Lalic',
    author_email='nick.lalic@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7',
    install_requires=['pycryptodome~=3.14.1', 'requests~=2.27.1'],
    extras_require={
        'dev':  ['twine', 'wheel'],
    },
    entry_points={
        'console_scripts': [
            'generate-walmart-auth-keys=walmart_auth.bin.generate_keys:main',
            'walmart-session=walmart_auth.bin.session:main'
        ]
    }
)
