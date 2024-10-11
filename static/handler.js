let letters = "abcdefghijklmnopqrstuvwxyz.";

async function animateElement(x) {
    return new Promise((resolve) => {
        let interval = null;
        let iteration = 0;

        interval = setInterval(() => {
            x.innerText = x.innerText
                .split("")
                .map((letter, index) => {
                    if (index < iteration) {
                        return x.dataset.value[index];
                    }

                    return letters[Math.floor(Math.random() * 26)];
                })
                .join("");

            if (iteration >= x.dataset.value.length) {
                clearInterval(interval);
                resolve();
            }

            iteration += 1 / 3;
        }, 30);
    });
}

async function animateAll() {
    const elements = document.getElementsByClassName("cryptic");

    for (let x of elements) {
        await animateElement(x);
    }
}

animateAll();
