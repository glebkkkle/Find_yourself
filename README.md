🌐 Overview

FindYourself is an AI-powered web application that guides students toward discovering their best-fit university major.
It combines psychometric analysis, adaptive questioning, and a fine-tuned large language model to generate deeply personalized suggestions.

The system uses:

🧭 A static quiz to establish a base personality and academic profile

🎯 An adaptive quiz that evolves dynamically based on previous answers

🤖 A fine-tuned Mistral 7B model, deployed locally via Llama.cpp, for reasoning and major recommendation

💬 An integrated chatbot, powered by the same fine-tuned model, to provide guidance and conversation

🧠 How It Works
1. Static Quiz — Personality & Core Traits

Students begin with a static quiz designed to collect baseline information about:

Interests

Academic strengths

Personality preferences

The fine-tuned model then synthesizes this into a personalized profile embedding.

2. Adaptive Quiz — Intelligent Refinement

Next, the adaptive quiz takes over.
Each new question is selected dynamically using cluster weights, which shift according to the student's previous answers.

This stage fine-tunes the AI’s understanding of the student’s:

Cognitive style

Academic tendencies

Potential alignment with major clusters (e.g., STEM, Arts, Business, Social Sciences, etc.)

3. Major Suggestion — AI-Generated Insight

After gathering quiz data and referencing the user’s generated profile,
the model produces a personalized major recommendation, along with reasoning and alternative suggestions.

The output is:

🧩 Context-aware

🎓 Data-driven

💡 Naturally interpretable and conversational

4. Chatbot — Ongoing Exploration

Students can continue exploring their options through a built-in chatbot.
The chatbot uses the same fine-tuned model to answer questions, explain reasoning, and discuss potential academic paths.

🧩 Tech Stack
Component	Technology
Frontend	HTML / CSS / JS / Shiny for Python
Backend	Python (FastAPI / Flask / Shiny)
AI Model	Mistral 7B fine-tuned with Unsloth
Inference Engine	Llama.cpp for local model execution
Adaptive Logic	Custom cluster-weighting mechanism
Data Generation	Custom synthetic dataset for model fine-tuning

🚀 Model Fine-Tuning Pipeline

🔹 Step 1: Dataset Generation

A custom dataset was generated to capture correlations between:

Student profiles

Quiz answers

Major outcomes

🔹 Step 2: Fine-Tuning with Unsloth

The Mistral 7B model was fine-tuned using Unsloth
 for efficient local adaptation:

LoRA-based parameter tuning

Reduced VRAM footprint

Optimized for reasoning tasks related to personality and recommendation

🔹 Step 3: Local Inference via Llama.cpp

The final model is served using Llama.cpp:

Runs locally

Low latency

Supports quantized formats (Q4–Q8)
