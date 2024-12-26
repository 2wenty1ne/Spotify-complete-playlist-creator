import { swapNotificationModalVisability } from "../notificationModal";

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

    //! TEST
    const errorButton: HTMLButtonElement = document.querySelector('.error-button') as HTMLButtonElement;
    if (!errorButton) {
        //! Internal Server Error
        console.log('HOME - error button not found');
        return;
    }
    console.log("error button pressed")

    errorButton.addEventListener('click', () => {
        swapNotificationModalVisability()
        console.log("error button clicked!");
    })
    //! TEST
}