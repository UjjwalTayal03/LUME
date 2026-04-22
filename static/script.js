async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const file = fileInput.files[0];

    let formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    document.getElementById("uploadStatus").innerText = data.message;
}


async function askQuestion() {
    const query = document.getElementById("query").value;

    const res = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
    });

    const data = await res.json();

    document.getElementById("answer").innerText = data.answer;
}