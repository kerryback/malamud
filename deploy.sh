#!/bin/bash

# Build and deploy script for Quarto website
echo "Rendering Quarto website..."
quarto render

echo "Adding files to git..."
git add .

echo "Committing changes..."
git commit -m "default"

echo "Pushing to origin main..."
git push origin main

echo "Deploy complete!"

echo "Opening browser to view docs/index.html..."
if command -v xdg-open > /dev/null; then
    xdg-open docs/index.html
elif command -v open > /dev/null; then
    open docs/index.html
elif command -v start > /dev/null; then
    start docs/index.html
else
    echo "Could not detect how to open browser. Please open docs/index.html manually."
fi