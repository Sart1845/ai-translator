const button = document.getElementById("translateBtn");


button.addEventListener("click", async function () {


    const text = document.getElementById("textInput").value;

    const language = document.getElementById("language").value;

    const result = document.getElementById("result");


    if(text.trim() === "") {

        result.innerHTML = "Please enter some text.";

        return;

    }


    result.innerHTML = "⏳ Translating...";


    try {


        const response = await fetch(
            "http://127.0.0.1:8000/translate",
            {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                text:text,

                language:language

            })

        });


        const data = await response.json();


        result.innerHTML = data.translation;


    }


    catch(error) {


        result.innerHTML =
        "❌ Unable to connect to server";


        console.log(error);

    }


});