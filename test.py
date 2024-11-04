import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image

def generate_image_from_text(prompt, output_image_path="generated_image.png"):
    # Load the pre-trained Stable Diffusion model
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Move model to GPU

    # Generate the image
    with autocast("cuda"):
        image = pipe(prompt).images[0]

    # Save the generated image
    image.save(output_image_path)
    print(f"Image saved at {output_image_path}")

# Example usage:
prompt = "A delicious breakfast with pancakes, eggs, and orange juice"
generate_image_from_text(prompt)