import { swapNotificationModalVisability } from "../notificationModal";
import { playlistPlaceholderSwap } from "./functions";
import { handleSubmitButton } from "./submitButton";

export function handleHome() {
    const artistIDSubmitButton = document.getElementById('submitArtistID');
    if (!artistIDSubmitButton) {
        console.error('Artist id submit button not found')
        return
    }

    //? Submit button
    artistIDSubmitButton.addEventListener('click', async () => {
        return await handleSubmitButton()
    })


    //? Login Button
    const logInButton: HTMLButtonElement = document.querySelector('.login-button') as HTMLButtonElement;
    if(!logInButton) {
        console.error('Login button not found')
        return;
    }
    
    logInButton.addEventListener('click', () => {

        const currentHost = window.location.origin;
        const loginPath = '/login';
        const loginUrl = `${currentHost}${loginPath}`;

        window.location.href = loginUrl;
    })


    //! TEST
    const transformButton: HTMLButtonElement = document.querySelector('.transform-button') as HTMLButtonElement;
    if(!transformButton) {
        console.error('Transorm button not found');
        return;
    }
    
    transformButton.addEventListener('click', () => {
        console.log('Transformed!'); //! TEST
        playlistPlaceholderSwap();
    })
    //! TEST


    //! TEST
    const errorButton: HTMLButtonElement = document.querySelector('.error-button') as HTMLButtonElement;
    if (!errorButton) {
        //! Internal Server Error
        console.log('HOME - error button not found');
        return;
    }

    errorButton.addEventListener('click', () => {
        swapNotificationModalVisability()
        console.log("error button clicked!");
    })
    //! TEST
}