# SciPy Proceedings Builder

- Customize `runserver.py` to update this year's branch.
  For debugging, enable ``ALLOW_MANUAL_BUILD_TRIGGER``.
- Install dependencies: ``pip install -r requirements.txt``
- Fetch PRs by running `./update_prs`
- Launch by running `runserver.py`

Note: the server has not been ported to Python 3 yet.

You need all the same dependencies as for building the proceedings as well:

 - IEEETran (often packaged as ``texlive-publishers``, or download from
   [CTAN](http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEtran/)
   LaTeX class
 - AMSmath LaTeX classes (included in most LaTeX distributions)
 - `docutils` 0.11 or later (``easy_install docutils``)
 - `pygments` for code highlighting (``easy_install pygments``)

```
sudo apt-get install python-docutils texlive-latex-base texlive-publishers \
                     texlive-latex-extra texlive-fonts-recommended
```
