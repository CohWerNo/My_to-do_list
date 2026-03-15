function saveFile(text="") {
    fetch("/save-text-in-file", {
        method:"POST",
        headers:{
            "content-type":"application/json",
        },
        body:JSON.stringify({text:text}),
    })
    .catch(error => console.error("error:", error))
}
document.addEventListener("input", function(event) {
    saveFile(event.target.value)
});