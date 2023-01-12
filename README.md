# Image-regeneration-using-Metropolis-Hastings-algorithm
The code regenerates a black and white image of any image input using Metropolis Hastings algorithm. 

The user inputs any image, and the Python code turns the image into a black and white image. Each pixel is thus given a value between 0 and 255. Every pixel is then normalized such that we get a normalized probability distribution in R^2 from the image itself. The Metropolis Hastings algorithm then samples from this distribution.
<p align="center">
  <img src="https://user-images.githubusercontent.com/121384892/212169187-cb618ca2-cb5e-4d03-a1a2-2d5314b403b6.png" width="500" />
  <img src="https://user-images.githubusercontent.com/121384892/212169205-b3322734-977e-4be7-9b76-0622dc8c1c66.png" width="500" /> 
</p>
Eventually, after many iterations, the converged probability distribution is plotted, and the image will successfully be recreated from pure randomness. See the images above.


