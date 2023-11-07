# Job Market Predictor

Job Market Predictor is a tool that fetches real-time job postings from Workable's API, analyzes them using the LLM app and its llm_app module, and predicts the job market's current status and future trends. It also employs Retrieval Augmented Generation (RAG) to provide enhanced insights and predictions.

## Technical Implementations

The project fetches real-time job postings from Workable's API. It uses the Pathway library and its llm_app module to process and analyze the fetched data. In addition, it employs RAG for enhanced analysis and prediction.

## How to Use

1. Clone the repository.
2. Install Docker on your machine.
3. Build the Docker image: `docker build -t job-market-predictor .`
4. Run the Docker container: `docker run -p 5000:5000 job-market-predictor`
5. Open the Streamlit app in your browser at `http://localhost:5000`.
