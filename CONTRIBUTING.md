Contributing
============

Contributions are always welcome. Every little help will be appreciated!

Furthermore, we love pull requests. Really!!!

However, to make your contribution more effective, we'll appreciate if you follow some guidelines.

How can I contribute with this project?
---------------------------------------

### Bug reports

Report bugs at [update-conf.py - Issues](https://github.com/rarylson/update-conf.py/issues) with the `Bug` flag.

If you are reporting a bug, please include:

- Your environment (operating system and version, python version, etc);
- Any other details about your local setup that might be helpful in troubleshooting;
- Detailed steps to reproduce the bug.

### Bugfixes

You can find all current opened bugs at [update-conf.py - Issues (Bug)](https://github.com/rarylson/update-conf.py/labels/bug).

Feel free to contribute solving any of these bugs.

When solving a bug, please add the bug reference in your commit message.

If you discovered a new bug and solved it, please create a bug report before submiting your solution.

### Implementing features

You can find all current proposed features in [README - TODO](README.md#TODO).

Feel free to contribute implementing any of these features.

If someday the number of features increases, we may move them to [update-conf.py - Issues (Enhancement)](https://github.com/rarylson/update-conf.py/labels/enhancement).

### Proposing features

For now, if you want to propose some feature, propose it at [update-conf.py - Issues](https://github.com/rarylson/update-conf.py/issues) with the `Enhancement` flag.

If you are proposing a feature, please:

- Explain in detail how it would work;
- Keep the scope as narrow as possible, to make it easier to implement.

Of course proposing a new feature will be welcome. But remember that this is a volunteer-driven project, and that contributions are welcome and awesome :smile:.

###  Write Documentation

You can help us improving the docs in the `README.md` file, in docstrings, in comments, and so on. They are the main docs about this project.

If you want, you can also help us writing about this project in articles, blogs, etc... You can even help fixing any English mistakes in the docs (sorry for them :cry:).

This is a very simple project. We thought it's easy to understand and to use. This is why it doesn't have much documentation. However, fell free to add more docs if you consider necessary.

Pull request guidelines
-----------------------

When creating a pull request, please try to follow these guidelines:

- Fork the project on Github;
- Base your changes in the develop branch;
    - You can use the master branch, but it would be possible that you lost some updates do not merged in the master branch yet;
    - Run:
      ```sh
      git clone git@github.com:YOUR_NAME/update-conf.py.git
      cd update-conf.py
      git checkout -b YOUR-BRANCH origin/develop
      ```
- For bugs and features, it's recomended to install the project in your local environmet inside a virtualenv;
  - The following setup might work at the most situations:
    ```sh
    virtualenv venv
    . venv/bin/activate
    pip install -r requirements-test.txt
    python setup.py develop
    ```
  - However, if you really need a complete environment, you can run (if you're using Ubuntu):
    ```sh
    make develop-deps-ubuntu
    make install-develop
    ```
- If your pull request solves a bug, include the necessary unit tests that reproduces the bug (and that passes after the fix);
- If your pull request adds a feature, include the necessary unit tests;
- Add any necessary docstrings and comments to the code;
- Verify if your code passes in every check and test:
  ```sh
  make check
  make test  # or 'sudo make test' to run all tests
  make test-coverage
  ```
- Push your changes:
  ```sh
  git push --set-upstream origin YOUR-BRANCH
  ```
- Make a pull request comparing your new branch with the project develop branch;
- Verify if your code works for Python 2.6, 2.7, 3.2, 3.3 and 3.4;
    - We're not using `tox` or a similar solution to do this. For now, check [update-conf.py - Travis CI - Pull requests](https://travis-ci.org/rarylson/update-conf.py/pull_requests) and make sure that your pull request tests pass for all supported Python versions.

If you follow all the previous guidelines, you're really an angel :angel: :+1:!

But if you can't follow all of them, DO NOT WORRY! Just submit your contribution! :smiley:
