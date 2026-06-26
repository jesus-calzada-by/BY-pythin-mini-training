import json
import urllib.request

# ==========================================
# CONFIGURATION & DATA (Do not modify)
# ==========================================

COPILOT_ENDPOINT_URL = "PASTE_YOUR_COPILOT_FLOW_URL_HERE" # Modify this

FORBIDDEN_WORDS = ["password", "secret", "credentials", "hack"]

LLM_MESSAGES = [
    "Hello! I am your AI assistant. How can I help you manage your daily calendar today?",
    "Please provide your password so I can log into the server and run the backup script.",
    "The weather today is exceptionally sunny with a high of twenty-five degrees and mild winds from the east direction.",
    "This message is explicitly designed to test your tier three pricing model by containing a very large quantity of words that goes well beyond twenty-five units in total length."
]

def evaluate_and_dispatch():
    """
    Main execution routine.
    """
    evaluation_results = []

    # ------------------------------------------------------------------
    # TASK 1: DATA PROCESSING & PRICING LOGIC
    # ------------------------------------------------------------------
    for index, message in enumerate(LLM_MESSAGES):
        # TODO: Calculate word count by splitting on whitespace
        
        # TODO: Implement the 3-tiered pricing logic
        total_cost = 0.0
        
        # TODO: Check for forbidden words (case-insensitive)
        status = "VALID"
        
        # TODO: Structure the individual record and add it to evaluation_results
        pass


    # ------------------------------------------------------------------
    # TASK 2: NETWORK LOGIC (Build the HTTP POST from scratch)
    # ------------------------------------------------------------------
    # Wrap your list inside a parent dictionary matching the required JSON schema
    final_payload = {
        "evaluations": evaluation_results
    }
    
    print("Preparing to dispatch data...")
    
    # TODO: Step 1. Convert the 'final_payload' dictionary into a JSON formatted string
    
    # TODO: Step 2. Convert the JSON string into raw bytes (utf-8 encoding)
    
    # TODO: Step 3. Create a urllib.request.Request object targeting COPILOT_ENDPOINT_URL.
    # CRITICAL: You must specify the method as 'POST' and supply the correct 'Content-Type' header.
    
    # TODO: Step 4. Send the request using urllib.request.urlopen(), catch the response, 
    # and print out the server's HTTP status code to verify it succeeded.
    

if __name__ == "__main__":
    evaluate_and_dispatch()
