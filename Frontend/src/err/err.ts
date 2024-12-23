export function handleErr() {
    const homeButton: HTMLButtonElement = document.querySelector('.return-home-button') as HTMLButtonElement;
    if (!homeButton) {
        console.log('home button not found');
        return;
    }

    homeButton.addEventListener('click', () => {
        const currentHost = window.location.origin;
        const homeURL = `${currentHost}/`;

        window.location.href = homeURL;
    })
}