import requests

url = "https://api.runpod.ai/v2/sdxl/runsync"
user_prompt=""
payload = { "input": {
        "prompt": user_prompt,
        "num_inference_steps": 50,
        "refiner_inference_steps": 60,
        "width": 1024,
        "height": 1024,
        "guidance_scale": 10,
        "strength": 0.5,
        "seed": None,
        "num_images": 1,
        "negative_prompt": "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs, missing arms, poorly drawn face, bad face, fused face, cloned face, worst face, three crus, extra crus, fused crus, worst feet, three feet, fused feet, fused thigh, three thigh, fused thigh, extra thigh, worst thigh, missing fingers, extra fingers, ugly fingers, long fingers, horn, extra eyes, huge eyes, 2girl, amputation, disconnected limbs, cartoon, cg, 3d, unreal, animate"
    } }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "APIKEY"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()
image_url = data["output"]["image_url"]

print(image_url)
