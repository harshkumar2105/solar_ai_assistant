
import gradio as gr
from utils import analyze_image

def process(image):
    result = analyze_image(image)
    return result

demo = gr.Interface(
    fn=process,
    inputs=gr.Image(type="pil"),
    outputs="json",
    title="Solar Rooftop Analyzer",
    description="Upload a satellite image of your rooftop to estimate solar panel suitability and ROI.",
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch()
