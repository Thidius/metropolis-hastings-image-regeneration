# Image regeneration using Metropolis Hastings algorithm
The code regenerates a black and white image of any image input using Metropolis Hastings algorithm. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/121384892/212169187-cb618ca2-cb5e-4d03-a1a2-2d5314b403b6.png" width="350" />
  <img src="https://user-images.githubusercontent.com/121384892/212169205-b3322734-977e-4be7-9b76-0622dc8c1c66.png" width="350" /> 
</p>

## Usage

1. Place the desired input image (`image.png`) in the directory specified in the code: `C:\Users\username\Desktop\image.png`. Replace `username` with your actual username.
2. Open the `image_to_matrix.py` script and run it using Python.

The script will perform the following steps:
1. Read the input image.
2. Convert the color image to a black and white image.
3. Create a matrix representing the normalized probability distribution over the image's pixel positions.
4. Use the Metropolis Hastings algorithm to sample from this distribution.
5. Generate a histogram-based visualization of the sampled positions.

The resulting plot will display the generated black and white image, representing the normalized probability distribution from the input image.

## How it Works

The script converts a color image to black and white by first converting the color channels to grayscale. Then, it creates a matrix `T` representing the normalized probability distribution over the image's pixel positions. The Metropolis Hastings algorithm is employed to sample from this distribution, generating a sequence of pixel positions.

## Contributing

Contributions are welcome! If you find any issues or ways to improve this script, feel free to create a pull request.

