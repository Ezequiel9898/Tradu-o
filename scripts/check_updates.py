name: Update Mods Status

on:
  schedule:
    - cron: "0 0 * * *"  # Executa diariamente
  workflow_dispatch:  # Permite execução manual

jobs:
  check-mod-updates:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install Dependencies
      run: pip install requests

    - name: Run Update Script
      run: python scripts/check_updates.py

    - name: Commit Changes
      run: |
        git config --global user.name "GitHub Actions"
        git config --global user.email "actions@github.com"
        git add .
        git commit -m "Atualização automática de status dos mods"
        git push
      continue-on-error: true
