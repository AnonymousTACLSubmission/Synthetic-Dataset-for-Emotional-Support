import openai
import pandas as pd

# OpenAI API key
openai.api_key = "Open AI Key"

# Path to the Excel file
excel_file_path = "generatedDataset.xlsx"

scenarios = 150

# Reading the excel file
sheet_name = "Dataset"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

#Loop to read the 150 different scenarios as different prompts
for i in range(scenarios):
    cell = "B" + str(i+2)  # The cell containing the prompt 
    prompt = df.at[i, 'Scenario context'] + " Based on the provided agent profiles and context, generate a conversation between both agents related to the context but focused on mental health topics such as depression, anxiety, emotional distress, and emotional support. Turn it into a situation where one agent is seeking emotional help and the other agent is providing emotional support but keep the conversation relevant to the context, goals and agent profiles given."
    conversations = 10

    # Loop to execute the prompt 10 times
    for j in range(conversations):
        print(f"Generating response {j+1}...")
        response = openai.chat.completions.create(
           model="gpt-4",  
           messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": prompt}
        ]
    )
    
        output = response.choices[0].message.content
        df.at[i, 'Conversation ' + str(j+1)] = output

# Writing to the excel file
df.to_excel(excel_file_path, index=False, engine="openpyxl")

print("Responses have been saved to the file!")
