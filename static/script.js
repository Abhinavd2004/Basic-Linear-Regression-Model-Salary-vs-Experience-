async function predictSalary() {
    const expInput = document.getElementById("experience");
    const resultDiv = document.getElementById("result");
    const experience = parseFloat(expInput.value);
  
    if (isNaN(experience)) {
      resultDiv.innerText = "Please enter a valid number.";
      return;
    }
  
    try {
      const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ experience }),
      });
      const data = await res.json();
      if (res.ok) {
        resultDiv.innerText = `Predicted Salary: $${data.predicted_salary.toFixed(2)}`;
      } else {
        resultDiv.innerText = `Error: ${data.error || "Something went wrong"}`;
      }
    } catch (err) {
      resultDiv.innerText = "Server unreachable.";
      console.error(err);
    }
  }
  
