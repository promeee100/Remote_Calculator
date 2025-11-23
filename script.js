function calculate() {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    const op = document.getElementById("op").value;

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ num1, num2, op }),
    })
        .then(response => response.json())
        .then(data => {
            const resultBox = document.getElementById("resultBox");
            resultBox.style.display = "block";
            resultBox.innerHTML = "Result: <strong>" + data.result + "</strong>";
        });
}
