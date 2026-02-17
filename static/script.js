function playGame(choice) {
    fetch(`/play/${choice}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("user").innerText =
                "You chose: " + data.user;

            document.getElementById("computer").innerText =
                "Computer chose: " + data.computer;

            document.getElementById("winner").innerText =
                "Result: " + data.result;
        });
}
