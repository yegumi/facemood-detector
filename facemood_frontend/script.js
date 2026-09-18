function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
}

async function sendImage() {
    // Step 1: GET request first, just to receive the CSRF cookie
    await fetch("http://127.0.0.1:8000/api/predict/", {
        method: "GET",
        credentials: "include"
    });

    const csrfToken = getCookie("csrftoken");

    const fileInput = document.getElementById("imageInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please choose an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    // Step 2: the actual POST, with the CSRF token attached
    const response = await fetch("http://127.0.0.1:8000/api/predict/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken
        },
        credentials: "include",
        body: formData
    });

    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
}