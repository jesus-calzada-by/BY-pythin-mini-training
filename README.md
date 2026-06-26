# AI Agent Evaluation & Automation Challenge

Welcome to the technical evaluation project! This challenge tests your problem-solving logic, data processing ability, and system integration skills rather than deep Python syntax. 

You are building a **Deterministic Evaluation Node** for an AI Agent pipeline. Your code will read a series of pre-generated LLM messages, evaluate them against specific business rules and tiered pricing models, and send the final evaluation to an automated Copilot orchestration endpoint.

---

## Project Objectives

1. Clone this repository locally.
2. Complete the logic inside `evaluator.py` to process the sample LLM messages.
3. Calculate token pricing based on a **3-tiered word-count model**.
4. Check messages against a **forbidden words filter**.
5. Issue an HTTP POST request containing your results to the designated Copilot endpoint.
6. Configure the Copilot cloud flow to log this data directly into SharePoint.

---

## Part 1: The Python Evaluation Logic

Open `evaluator.py` in your editor. You will see a list of pre-written messages. For **each** message, your logic must compute the following:

### 1. Word Count Calculation
To calculate costs, you must first determine the number of words in a message. 
* Split the message text using white spaces as delimiters to count the words.

### 2. Tiered Pricing Model
The cost of an LLM generation is calculated dynamically using three tiers based on word count:
* **Tier 1 (Base)**: The first **10 words** cost **$0.02 per word**.
* **Tier 2 (Mid)**: The next **15 words** (words 11 through 25) cost **$0.015 per word**.
* **Tier 3 (Max)**: Any words **above 25 words** cost **$0.005 per word**.

*Example:* A message with 28 words would cost:
`(10 * 0.02) + (15 * 0.015) + (3 * 0.005)`

### 3. Compliance Filter
If a message contains **any** word listed in the `FORBIDDEN_WORDS` array, its status must immediately be flagged as `"INVALID"`. If it does not contain any forbidden words, its status is `"VALID"`. 
* *Note:* The check should be case-insensitive (e.g., "secret" and "SECRET" should both trigger the filter).

---

## Part 2: Copilot Flow & SharePoint Integration

Once your script compiles the evaluations, it must trigger an automation flow.

1. **Get the Endpoint**: The Copilot flow will be shared with you directly. You must open the shared flow in your environment and extract its unique HTTP POST URL endpoint from there to use in your script.
2. **Modify the Flow**: Open your designated Copilot/Power Automate environment. Adjust the flow triggered by this HTTP POST request to map the incoming JSON payload fields.
3. **Log to SharePoint**: Add a step in the flow that inserts the payload data into the specified SharePoint List, tracking the message index, word count, total cost, and compliance status.

---

## Expected JSON Payload Format

Your Python script must format the final payload exactly like this before sending the POST request:

```json
{
  "evaluations": [
    {
      "message_index": 0,
      "word_count": 14,
      "total_cost": 0.26,
      "status": "VALID"
    },
  ]
}
```

Good luck! Focus on the logical flow of variables, order of operations, and handling edge cases correctly.
