const copyBtns = [...document.getElementsByClassName('copy-btn')]

let previous = null

copyBtns.forEach(btn => btn.addEventListener('click', () => {
    const color = btn.getAttribute('data-hex')
    navigator.clipboard.writeText(color)

    navigator.clipboard.readText().then(clipText => {
        btn.textContent = `url copied`
    })

    if (previous) {
        previous.textContent = 'click'
    }
    previous = btn
}))



