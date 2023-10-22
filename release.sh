# Only for fist setup
#py2applet --make-setup PDFViezzer.py

# Clean
rm -rf build dist

# Run
python3 setup.py py2app

# Move to app folder
mv dist/VEZSplitter.app /Applications