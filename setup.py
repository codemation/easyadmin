import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='easyadmin',  
     version='NEXTVERSION',
     packages=setuptools.find_packages(include=['easyadmin', 'easyadmin.pages', 'easyadmin.elements'], exclude=['build']),
     author="Joshua Jamison",
     author_email="joshjamison1@gmail.com",
     description="Generate pre-formatted HTML elements for an Admin type front-end",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/codemation/easyadmin",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.7, <4',   
     install_requires=[], )