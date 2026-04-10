import sys

try:
    import pandas as pd
    import pycaret
    import autoviz
    import ydata_profiling
    print(f"✅ Success! Python {sys.version.split()[0]} is ready.")
    print(f"✅ All tools are installed and imported.")
except ImportError as e:
    print(f"❌ Error: {e}")
    print("Double-check that you activated your venv and ran 'pip install -r requirements.txt'")
