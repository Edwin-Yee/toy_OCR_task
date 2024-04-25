# OCR coding task for research position

This repository constitutes a coding problem aimed at assessing your ability to work with GitHub, Python, and basic OCR tools. You are welcome (and even encouraged to) use AI such as ChatGPT to help you with this, and please do not hesitate to reach out to annaboser@ucsb.edu if you have any questions about the problem or need a hint. We expect this will take you approximately 2 hours to complete. Email your solution to annaboser@ucsb.edu and ahilton@ucsb.edu by your interview time.

## Instructions: 

This problem requires you to digitize the numbers in the `data` folder of this directory. These numbers were pulled from a historical hydrological document like the one we would be working to digitize. To do so: 

1. Fork this repository to create your own to work out of. Make it a public repository. Clone it to your local computer. 
1. Create a `code/` folder. Write Python code in this folder which generates an `output.txt` file (housed in the main repository). This file will list all the numbers written on the images in the `data/` folder in the order of their image name (i.e. `image_1.png`, then `image_2.png`, etc.) , with a new number on each new line. 
1. Run your python code to generate the `output.txt` file. It's 100% fine if all the numbers are not correct. 
1. Document your work (see below for detailed instructions). Make sure everything is committed and pushed. 
1. Email a link you your completed forked repository to annaboser@ucsb.edu and ahilton@ucsb.edu by your interview time. Please ensure it is public so we can review it. 

### By the end of the problem, your repository should include: 
1. A `requirements.txt` or similar file with all the Python packages required to run your code specified and a filled out section to the readme (see below) with setup instructions such that I can easily recreate your environment and run your code
1. A `code` folder containing all the Python code necessary to generate the output file and a filled out section of the readme explaining these contents and how to run the code. Please additionally ensure that the code is properly commented and easily readable. 
1. The `output.txt` file containing the numbers printed on the documents in the data folder, in order and with a new line for each new entry. 

## Setup instructions 
Create and Run Virtual Environment
- python3 -m venv venv  (this line only needs to be run one time)
- source venv/bin/activate (this line must be run to activate the virtual environment)

Install Pytesseract for OCR task
- The following three lines only need to run once:
- pip install pytesseract
- brew install tesseract (for Mac users make sure you have Homebrew installed!)
- Retrieve starter code from documentation: https://pypi.org/project/pytesseract/ using GitHub Desktop (or git clone)

## Instructions to reproduce the output 
- git clone the repository (easiest way is to download GitHub Desktop)
- cd into the code folder in terminal
- run: python3 digitize_numbers.py 

The `output.txt` file contained in this repository was generated with the code available in the `code/` folder. The current version achieves a 93.33% accuracy on the given images, missing "12" at index 13, and ".66" at index 18.

## Reference
- Review the Tesseract Documentation
- By running the command: tesseract --help-extra, we are able to see the different possible configurations for OCR image detection by tesseract. I have highlighted the most relevant portions (OEM: OCR Engine Mode, PSM: Page Segmentation Mode) below

Usage:
  tesseract --help | --help-extra | --help-psm | --help-oem | --version
  tesseract --list-langs [--tessdata-dir PATH]
  tesseract --print-fonts-table [options...] [configfile...]
  tesseract --print-parameters [options...] [configfile...]
  tesseract imagename|imagelist|stdin outputbase|stdout [options...] [configfile...]

OCR options:
  --tessdata-dir PATH   Specify the location of tessdata path.
  --user-words PATH     Specify the location of user words file.
  --user-patterns PATH  Specify the location of user patterns file.
  --dpi VALUE           Specify DPI for input image.
  --loglevel LEVEL      Specify logging level. LEVEL can be
                        ALL, TRACE, DEBUG, INFO, WARN, ERROR, FATAL or OFF.
  -l LANG[+LANG]        Specify language(s) used for OCR.
  -c VAR=VALUE          Set value for config variables.
                        Multiple -c arguments are allowed.
  --psm NUM             Specify page segmentation mode.
  --oem NUM             Specify OCR Engine mode.
NOTE: These options must occur before any configfile.

Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.

OCR Engine modes:
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.

Single options:
  -h, --help            Show minimal help message.
  --help-extra          Show extra help for advanced users.
  --help-psm            Show page segmentation modes.
  --help-oem            Show OCR Engine modes.
  -v, --version         Show version information.
  --list-langs          List available languages for tesseract engine.
  --print-fonts-table   Print tesseract fonts table.
  --print-parameters    Print tesseract parameters.


Here are some guides that I referenced:
- https://pypi.org/project/pytesseract/ 
- https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/ 
- https://ai-facets.org/tesseract-ocr-best-practices/ 

