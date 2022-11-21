import setuptools

setuptools.setup(
        name = 'rikai',
        packages = setuptools.find_packages(),
        install_requires=[
            'numpy', 'torch', 'tqdm'],
        entry_points = {
            'console_scripts':[
                'rikai = rikai.cli.main']})

