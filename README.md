# Mezuzah-Checker
OCR algorithm to check if there are any missed, added or wrong letters in a mezuzah.

For now, the algorithm finds the letters in the image, order them and recognize the letters by pre-trained tensorflow model.

# Example  
The base image  
<img src="https://github.com/ari-github/Mezuzah-Checker/blob/main/images/mz1.jpg" width="500">

Rectangles around the letters (different color for each row)  
<img src="https://github.com/ari-github/Mezuzah-Checker/blob/main/images/rows.jpg" width="500">
  
Recognised letters (the numbers represent the letter's [gematria](https://en.wikipedia.org/wiki/Gematria))
![alt text](https://github.com/ari-github/Mezuzah-Checker/blob/main/images/prediction.jpg)

