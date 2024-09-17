### Assignment Overview

**Objective:**  
Create a basic Web UI that simulates an AI sales agent responding to customer inquiries based on questions provided in a transcript.

**Scenario:**  
You are tasked with developing a minimal viable product (MVP) for an AI sales agent. It will read questions from text file and get product data from the product website and answer the questions provided in the text file

**Requirements:**

1. **Input:**  
   1. You will be provided with a text file containing a series of questions typically asked by customer .Each question is on a separate line.
   2. The product website URL from which you can scrap the data. Use AI tool APIS/Python Package available to scrap the data from website

2. **Output:**  
   The Web UI should read the input questions, process them, and generate appropriate responses. Responses should be structured and informative, drawing information primarily from a specified product website. Display the answer on the WEB UI
   Also get data from the website using some script at backend (DONT USE SOME AI TOOL UI TO GET THE TEXT INSTEAD OBTAIN IT USING SOME TOOL API/Python Package at BACKEND)

3. **Functionality:**
   - Retrieve relevant data from the product website to answer each question.
   - Formulate responses that are clear, concise, and tailored to the specific question asked.


4. **Deliverables:**
   - A simple UI with backend which accepts text file that reads the input text file,takes website URL as input and generates responses to each question based on information provided on website
   - Upload all the artificats on GitHub and share the link via email

5. **Resources:**
   - The product website URL: https://www.tp-link.com/in/home-networking/smart-plug/hs100/
   - Questions text: It is provided at the end
   - OpenAI/Anthropic/Any other LLM API key you can get from relevant website
   - Any AI tool API or python package to extract text from website

**Assessment Criteria:**

- How well does the script extract and utilize information from the product website to answer questions?
- Code quality and structure: Is the code well-organized, readable, and appropriately documented?

**Additional Notes:**

- The focus of this assignment is on functionality and basic implementation.
- Candidates are encouraged to use libraries or APIs for web scraping, and text generation as needed.
- Avoid over-engineering. The goal is to create a functional prototype that demonstrates the core capabilities of the AI sales agent.

**Example Transcript:**

```
    1. How can the HS100 V3 Wi-Fi Smart Plug be controlled remotely, and what app is used for this purpose?
    2. What scheduling features does the HS100 V3 Wi-Fi Smart Plug offer for managing household electronics?
    3. Describe the security features of the HS100 V3 Wi-Fi Smart Plug that create the appearance of someone being home.
    4. What are the dimensions and weight of the HS100 V3 Wi-Fi Smart Plug?
    5. How does the design of the HS100 V3 Wi-Fi Smart Plug blend with modern home decor, and what is the benefit of its countdown timer feature?
```


