# Python formatting

This project uses [ruff](https://github.com/astral-sh/ruff) for code formatting, import sorting, and linting.

All code that is contributed to AutoPkg must match these style requirements. These
requirements are enforced by [pre-commit](https://pre-commit.com).

## Use relocatable-python to safely build 3

We recommend using Greg Neagle's [Relocatable Python](https://github.com/gregneagle/relocatable-python) to build a custom Python 3 framework. While the repository no longer tracks `requirements.txt` directly (as `pyproject.toml` is the source of truth), you can generate one using [uv](https://github.com/astral-sh/uv):

```sh
uv export --format requirements-txt --no-hashes --no-header --no-dev -o requirements.txt
```

First, create a safe path to place your frameworks. The easiest choice is
/Users/Shared, because you won't have any permissions issues there, but you can
place this anywhere that makes sense to you:

```sh
mkdir -p /Users/Shared/Python3
```

Now create your relocatable Python frameworks using the generated requirements.txt file:

```sh
./make_relocatable_python_framework.py --python-version 3.10.11 --pip-requirements /path/to/requirements.txt --destination /Users/Shared/Python3/
```

### Symlink the frameworks

You can symlink in the python executables into a more useful path:

```sh
sudo ln -s /Users/Shared/Python3/Python.framework/Versions/3.7/bin/python3 /usr/local/bin/python3_custom
```

## Use pre-commit to set automatic commit requirements

This project makes use of [pre-commit](https://pre-commit.com/) to do automatic
lint and style checking on every commit containing Python files.

To install the pre-commit hook, run the executable from your Python 3 framework
while in your current autopkg git checkout:

```sh
cd ~/autopkg
/Users/Shared/Python3/Python.framework/Versions/3.7/bin/pre-commit install --install-hooks
```

Once installed, all commits will run the test hooks. If your commit fails any of
the tests, the commit will be rejected.

### Example of a failed commit

```sh
git commit -m "test a bad commit for pre-commit"
```

```console
ruff.....................................................................Failed
hookid: ruff

Code/autopkglib/AppDmgVersioner.py:1:1: I001 [*] Import block is un-sorted or un-formatted
Found 1 error.
[*] 1 fixable with the `--fix` option.

ruff-format..............................................................Failed
hookid: ruff-format

1 file reformatted

flake8...................................................................Failed
hookid: flake8

Code/autopkglib/AppDmgVersioner.py:31:1: E303 too many blank lines (3)
```

### Example of a successful commit

```sh
git commit -m "test a good commit for pre-commit"
```

```console
ruff.....................................................................Passed
ruff-format..............................................................Passed
flake8...................................................................Passed
[test ebe7fea] test2 for pre-commit
 1 file changed, 3 insertions(+)
```
