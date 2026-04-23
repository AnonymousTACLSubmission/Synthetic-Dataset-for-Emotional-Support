import openai
import pandas as pd

# OpenAI API key
openai.api_key = "Open AI Key"

# Path to the Excel files
readFrom_excel_file_path = "generatedDataset.xlsx"
writeTo_excel_file_path = "datasetRefinement.xlsx"

scenarios = 150

# Reading the excel file
readFrom_sheet_name = "Dataset"
writeTo_sheet_name = "Emotion expressed"
df = pd.read_excel(readFrom_excel_file_path, sheet_name=readFrom_sheet_name)

#Loop to read the 1500 conversations and annotate the emotion expressed

for i in range (scenarios):
     conversations = 10
     print(""Scenario"" + str(i+1))
     for j in range(conversations):  
      print(""Conversation"" + str(j+1)) 
      prompt = df.at[i, 'Conversation ' + str(j+1)] + ""Based on the conversation provided between an emotional help seeker and an emotional supporter, please identify the emotion expressed by the emotional help seeker from the following emotions: anxiety, depression, sadness, anger, fear, shame, disgust. Please provide the response only as one or two words representing the emotion identified. Do not provide the answer as \""The emotion expreesed by Isabella is sadness\"", instead just provide the answer in one word as \""Sadness\"""" 
      print(f""Generating response {j+1}..."")
      response = openai.chat.completions.create(
      model=""gpt-4"",  
      messages=[
      {""role"": ""system"", ""content"": ""You are a helpful assistant.""},
      {""role"": ""user"", ""content"": prompt}
      ]
    )
      output = response.choices[0].message.content
      df.at[i, 'Conversation ' + str(j+1)] = output

# Writing to the excel file
df.to_excel(writeTo_excel_file_path, sheet_name = writeTo_sheet_name, index=False, engine=""openpyxl"")

print(""Responses have been saved to the file!"")"
