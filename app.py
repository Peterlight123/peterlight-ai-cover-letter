import gradio as gr
from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="google/flan-t5-small"
)

def generate_cover_letter(cv, job):

    prompt = f"""
Write a short, professional, and human cover letter based on the CV and job description.

CV:
{cv}

Job description:
{job}

Cover letter:
"""

    result = generator(prompt, max_new_tokens=200)[0]["generated_text"]

    return result


with gr.Blocks(title="Peterlightspeed AI Cover Letter Generator") as demo:

    gr.Markdown("""
# Peterlightspeed – AI Resume & Cover Letter Generator

Built by **Peterlightspeed**  
Hybrid Frontend & AI Developer

Email: petereluwade55@gmail.com  
Portfolio: https://peterlight123.github.io/portfolio  
LinkedIn: https://tinyurl.com/eluwadelinkedin
X (Twitter): https://x.com/peterlightspeed
---
""")

    cv = gr.Textbox(label="Paste your CV", lines=8)
    job = gr.Textbox(label="Paste Job Description", lines=8)

    btn = gr.Button("Generate Cover Letter")

    output = gr.Textbox(label="Generated Cover Letter", lines=12)

    btn.click(generate_cover_letter, [cv, job], output)

demo.launch()
