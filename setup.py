import setuptools

setuptools.setup(
    name='github-delete',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/github-delete']
)
