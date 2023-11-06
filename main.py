import pathway as pw
from api import fetch_jobs
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import llm_app

# Fetching the job postings data
jobs = fetch_jobs()

# Creating a data stream
table = pw.demo.from_list(jobs)

# Using llm_app module for processing
processed_table = llm_app.process(table)

# Using RAG for enhanced analysis and prediction
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

# Generating predictions for job market trends
inputs = tokenizer(processed_table, return_tensors="pt")
generated = model.generate(inputs.input_ids)
predictions = tokenizer.batch_decode(generated, skip_special_tokens=True)

# Storing predictions into a CSV file
pw.io.csv.write(predictions, "predictions.csv")

# Now that the pipeline is built, the computation is started
pw.run()
