# How to use


# How to use

## Setting up pyenv

`pyenv` is a simple, powerful tool for managing multiple Python versions on your system. Follow these steps to set it up and use it:

### 1. Install pyenv

First, you need to install `pyenv`. You can do this using `curl`:

```sh
curl https://pyenv.run | bash
```

### 2. Set up your shell environment
After installing pyenv, you need to add it to your shell's configuration file. Add the following lines to your .bashrc, .zshrc, or .profile file:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

```sh
exec "$SHELL"

source ~/.bashrc
```

### 3. Install Python versions
You can now install different Python versions using pyenv. For example, to install Python 3.8.6, run:

```sh
pyenv install [VERSION]

pyenv global [VERSION]

pyenv local [VERSION]

python --version

pyenv uninstall [VERSION]
```

# Poetry 

To create a new project

```sh
poetry init
```

To run a script

```sh
which python

poetry run which python

poetry shell

which python
```

To add a new dependency

```sh
poetry add library
```

To install dependencies

```sh
poetry install
```
