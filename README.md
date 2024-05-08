# Environment Setup

## Initial venv Installation

Navigate to your source directory, and run the following command.

```
python3 -m venv env
```

## Activate Virtual Environment

On mac, activate virtual environment with:

```
source env/bin/activate
```

On windows, activate the virtual environment:

```
env/Scripts/activate.bat // In CMD
env/Scripts/Activate.ps1 // In Powershell
```

# Development

## Package Updates

To enable package updates, run the following command ONCE:

```
pip install pipreqs
```

To update packages, run the following from the home directory:

```
pipreqs . --force
```

## Package Management

To install packages, run the following:

```
pip install -r requirements.txt
```
