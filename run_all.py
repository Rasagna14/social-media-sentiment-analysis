import subprocess

scripts = [
    'scripts/1_data_collection.py',
    'scripts/2_text_cleaning.py',
    'scripts/3_sentiment_analysis.py',
    'scripts/4_keyword_extraction.py',
    'scripts/5_save_results.py'
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", script])