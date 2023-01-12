# Image-regeneration-using-Metropolis-Hastings-algorithm
The code regenerates a black and white image of any image input using Metropolis Hastings algorithm. 

The user inputs any image, and the Python code turns the image into a black and white image. Each pixel is thus given a value between 0 and 255. Every pixel is then normalized such that we get a normalized probability distribution in R^2 from the image itself. The Metropolis Hastings algorithm then samples from this distribution.

![MH-bild](https://user-images.githubusercontent.com/121384892/212169005-71db5dca-a333-4816-8930-4605be9cc709.png) ![Katt](https://user-images.githubusercontent.com/121384892/212169113-2dc69917-3665-4347-95bc-7aa54b01b2b3.png)

Eventually, after many iterations, the converged probability distribution is plotted, and the image will successfully be recreated from pure randomness. 

The more pixelated a image is, the more iterations will be needed to get a detailed enough image. The code has been published in a Jupyter Notebook.
