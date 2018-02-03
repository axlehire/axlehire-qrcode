"""
Setup tool
"""


from setuptools import setup


setup(name='myqr',
      version='1.0',
      description='',
      url='https://github.com/axlehire/axlehire-qrcode',
      author='Long Tran',
      author_email='long@axlehire.com',
      packages=[
            'MyQR',
            'MyQR.mylibs'
      ],
      include_package_data=True,
      install_requires=['imageio', 'numpy', 'Pillow'],
      zip_safe=False)