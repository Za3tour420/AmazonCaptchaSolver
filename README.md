# AmazonCaptchaSolver

Small Amazon captcha solver using OCR that can be implemented in your Amazon scraping projects.

## How it works
If the captcha is triggered, the image will be requested (image url is within the HTML code of the page), the text will be extracted using easyocr. It will then fill out the field and confirm the input.

There are still some minor adjustments to be made.
