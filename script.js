document.getElementById("claimForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const customerName = document.getElementById("customerName").value;
    const claimType = document.getElementById("claimType").value;
    const claimAmount = Number(document.getElementById("claimAmount").value);
    const policyFile = document.getElementById("policyFile").files[0];

    const formData = new FormData();

    formData.append("customer_name", customerName);
    formData.append("claim_type", claimType);
    formData.append("claim_amount", claimAmount);
    formData.append("policy_file", policyFile);

    const response = await fetch("http://127.0.0.1:8000/claims", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").textContent = data.status;
});


