function processExpression() {
    let expression = document.getElementById("expression").value;
    let operation = document.getElementById("operation").value;
    let resultDisplay = document.getElementById("result");
    let stackTable = document.querySelector("#stackTable tbody");

    if (!expression) {
        resultDisplay.innerHTML = "Please enter an expression!";
        return;
    }

    resultDisplay.innerHTML = "Processing...";
    stackTable.innerHTML = ""; // Clear previous table

    let endpoint = "";
    let requestData = { expression: expression };

    if (operation.includes("evaluation")) {
        endpoint = "/evaluate";
        requestData.eval_type = operation.replace("_evaluation", "");
    } else {
        endpoint = "/convert";
        requestData.conversion_type = operation;
    }

    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        resultDisplay.innerHTML = data.result;

        if (data.steps.length > 0) {
            data.steps.forEach((step, index) => {
                let row = stackTable.insertRow();
                row.insertCell(0).innerText = index + 1;
                row.insertCell(1).innerText = step.symbol;
                row.insertCell(2).innerText = step.stack ? step.stack.join(" ") : "";
                row.insertCell(3).innerText = step.output ? step.output.join(" ") : "";
            });
        } else {
            let row = stackTable.insertRow();
            row.insertCell(0).colSpan = 4;
            row.insertCell(0).innerText = "No step-by-step data available.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        resultDisplay.innerHTML = "Error processing request.";
    });
}
