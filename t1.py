import os
from pathlib import Path
data_dir = Path('/Users/harsh/PycharmProjects/spam_classifier/data')
emails = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]