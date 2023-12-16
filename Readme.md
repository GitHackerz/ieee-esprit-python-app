# IEEE ESPRIT SB Python APP

## Setup

### Setup virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

```bash
./venv/Scripts/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

### Build the app
```bash
pyinstaller --onefile --windowed app.py
```