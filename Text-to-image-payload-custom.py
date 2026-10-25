import time
import requests
from PIL import Image
from io import BytesIO
from config import HUGGINGFACE_API_KEY as HF_API_KEY

MODEL_ID = "stabilityai/stable-diffusion-3-medium-diffusers"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Accept": "image/png",
    "Content-Type": "application/json"
}

def _extract_err(r: requests.Response) -> str:
    try:
        data = r.json()

        if isinstance(data, dict):
            error = data.get("error")

            if isinstance(error, dict):
                return error.get("message") or str(data)

            return error or str(data)

        return str(data)

    except Exception:
        return (r.text or "").strip() or r.reason or "Request failed."

def generate_image_from_text(prompt: str, negative_prompt: str = None) -> Image.Image:
    payloads = []

    if negative_prompt:
        payloads.append({
            "inputs": {
                "prompt": prompt,
                "negative_prompt": negative_prompt
            }
        })
        payloads.append({
            "inputs": prompt,
            "parameters": {
                "negative_prompt": negative_prompt
            }
        })
        payloads.append({
            "inputs": prompt,
            "options": {
                "negative_prompt": negative_prompt
            }
        })

    payloads.append({"inputs": {"prompt": prompt}})
    payloads.append({"inputs": prompt})

    last_err = None

    for payload in payloads:
        for attempt in range(3):
            try:
                response = requests.post(
                    API_URL,
                    headers=HEADERS,
                    json=payload,
                    timeout=120
                )
            except requests.RequestException as error:
                last_err = f"Request failed: {error}"
                break

            content_type = (
                response.headers.get("Content-Type") or ""
            ).lower()

            if response.status_code == 200 and content_type.startswith("image/"):
                return Image.open(BytesIO(response.content))

            last_err = f"{response.status_code}: {_extract_err(response)}"

            if response.status_code in (502, 503, 504):
                time.sleep(1 + attempt)
                continue

            break

    raise Exception(
        last_err or "The response was not an image. Check the API response."
    )

def main():
    print("=== Text-to-Image Generator ===")
    print("Type 'exit' to close the program.\n")

    while True:
        prompt = input("Enter your image prompt:\n> ").strip()

        if prompt.lower() == "exit":
            print("See you next time!")
            break

        if not prompt:
            print("Please enter a prompt.\n")
            continue

        neg_input = input(
            "Enter a negative prompt (or press Enter to skip):\n> "
        ).strip()

        negative_prompt = neg_input if neg_input else None

        print("\nImage Settings:")
        print(f"Prompt: {prompt}")
        print(f"Negative Prompt: {negative_prompt or 'None'}")
        print("Generating image, please wait...\n")

        try:
            image = generate_image_from_text(
                prompt,
                negative_prompt=negative_prompt
            )

            image.show()

            save_option = input(
                "Save the image? (yes/no): "
            ).strip().lower()

            if save_option == "yes":
                file_name = input(
                    "Enter a filename without the extension: "
                ).strip() or "generated_image"

                file_name = "".join(
                    char for char in file_name
                    if char.isalnum() or char in ("_", "-")
                ).rstrip()

                if not file_name:
                    file_name = "generated_image"

                image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")

        except Exception as error:
            print(f"Something went wrong: {error}\n")

        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()
