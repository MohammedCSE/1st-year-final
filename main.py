from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import save_claim
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Insurance policies
policies = {
    "Med": 500,
    "Pres": 1000
}


# What a claim should contain
class Claim(BaseModel):
    customer_name: str
    claim_type: str
    claim_amount: float


# Claim checking logic
def check_claim(claim_type, claim_amount):

    if claim_type in policies:
        coverage_limit = policies[claim_type]

        if claim_amount <= coverage_limit:
            return "Claim can be processed."
        else:
            return "Claim exceeds the coverage limit."

    elif claim_type == "Dental":
        return "Dental treatment is not covered."

    else:
        return "Invalid claim type."


# API endpoint
@app.post("/claims")
async def create_claim(
    customer_name: str = Form(...),
    claim_type: str = Form(...),
    claim_amount: float = Form(...),
    policy_file: UploadFile = File(...)
):

    print("Customer:", customer_name)
    print("Claim type:", claim_type)
    print("Claim amount:", claim_amount)
    print("Uploaded file:", policy_file.filename)

    return {
        "status": "Claim received!",
        "file_name": policy_file.filename
    }

