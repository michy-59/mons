#!/bin/bash
python3 scr/create_view.py
RESULT=$(python3 scr/count.py)

git add .
git commit -m "$RESULT mons"
git push