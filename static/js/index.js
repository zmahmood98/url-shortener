let enterURL = document.getElementById("url")
let enterID = document.getElementById("custom_id")
let reset = document.getElementById("resetButton")

reset.addEventListener('click', () => {
    enterURL.value = ""
    enterID.value = ""
})
