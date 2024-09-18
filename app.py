import gradio as gr
from scraper import web_content
from content_remover import final_content
from answer_generator import question_answerer

def process_questions(product_url, questions):
    if not product_url or not questions:
        return "Please provide both product URL and questions."
    content = web_content(product_url)
    responses = []
    for question in questions.split("\n"):
        if question.strip():  
            relevant_content = final_content.invoke({"content" :content, "question":question})
            answer = question_answerer.invoke({"content": relevant_content, "question": question})
            responses.append(f"Question: {question}\nAnswer: {answer.template_compatibility}")
    
    return "\n\n".join(responses)

def chat_interface(product_url, questions):
    return process_questions(product_url, questions)

with gr.Blocks() as demo:
    gr.Markdown("## Product Q&A Chatbot")

    product_url_input = gr.Textbox(label="Product Website URL", placeholder="Enter product website URL")
    questions_input = gr.Textbox(label="Questions", placeholder="Enter customer questions (one per line)", lines=5)
    
    chatbot_output = gr.Textbox(label="Responses", interactive=False)
    
    submit_button = gr.Button("Generate Answers")
    
    submit_button.click(fn=chat_interface, inputs=[product_url_input, questions_input], outputs=chatbot_output)

if __name__ == "__main__":
    demo.launch()
