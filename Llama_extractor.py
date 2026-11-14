import json
from huggingface_hub import InferenceClient

client = InferenceClient(model="http://localhost:8080/v1")

job_scheme = {
    "type": "object",
    "properties": {
        "role": {"type": "string"},
        "tech_stack": {"type": "array", "items": {"type": "string"}},
        "year_experience": {"type": "integer"},
        "is_remote": {"type": "boolean"},
    },
    "required": [
        "role",
        "tech_stack",
        "year_experience",
        "is_remote",
    ],
    "additionalProperties": False,
}

messy_input = (
    "We urgently need a full-stack developer who is comfortable with React,"
    " Node.js, and Docker. Needs around 3 years of experience. This position"
    " is fully remote."
)

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {
            "role": "system",
            "content": "Extract the required job details from the text.",
        },
        {"role": "user", "content": messy_input},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "job_extraction",
            "strict": True,
            "schema": job_scheme,
        },
    },
    temperature=0.0,
)

raw_output = response.choices[0].message.content
structured_data = json.loads(raw_output)

print("--- Successfully Parsed Python Dictionary ---")
print(structured_data)
print(f"\nData type: {type(structured_data)}")
print(f"Extracted Role: {structured_data['job_title']}")
print(f"Tech Stack Array: {structured_data['job_requirements']['required_skills']}")
print(f"Years of Experience: {structured_data['job_requirements']['years_of_experience']}")

