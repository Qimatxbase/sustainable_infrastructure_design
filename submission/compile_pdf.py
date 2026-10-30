#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Paths
    submission_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(submission_dir)
    html_file = os.path.join(submission_dir, "master_report.html")
    pdf_file = os.path.join(submission_dir, "final_submission.pdf")
    
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    if not os.path.exists(html_file):
        print(f"Error: HTML file not found at {html_file}")
        sys.exit(1)
        
    if not os.path.exists(chrome_path):
        print(f"Error: Google Chrome not found at {chrome_path}")
        sys.exit(1)
        
    print(f"Compiling {html_file} to {pdf_file} using headless Chrome...")
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    
    try:
        # Run headless Chrome print-to-pdf
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(pdf_file):
            size = os.path.getsize(pdf_file)
            print(f"Success! PDF created successfully at: {pdf_file}")
            print(f"File size: {size / 1024:.2f} KB")
        else:
            print("Error: Command executed but PDF file was not generated.")
            print(result.stderr.decode('utf-8'))
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with error: {e}")
        print("Stdout:", e.stdout.decode('utf-8'))
        print("Stderr:", e.stderr.decode('utf-8'))
        sys.exit(1)

if __name__ == "__main__":
    main()
