
export function handleModal() {
    const modalCloseButton: HTMLButtonElement = document.querySelector('#close-modal-button') as HTMLButtonElement;
    if (!modalCloseButton) {
        //! Internal Server Error
        console.error('GLOBAL - notification modal close button not found')
        return
    }
    
    modalCloseButton.addEventListener('click', () => {
        try {
            var notificationModalBlur = getNotificationModalBlurElement()
        } catch (err) {
            return;
        }
        hideNotificationModal(notificationModalBlur)
    });
}

export function sendNotifactionModal() {
    try {
        var modalElement = getNotificationModalBlurElement()
    } catch (err) {
        console.error(err.message)
        return;
    }
    
} 


export function getNotificationModalBlurElement() {
    const notificationModalBlur: HTMLDivElement = document.querySelector('#notification-modal-blur-background') as HTMLDivElement;
    if (!notificationModalBlur) {
        //! Internal Server Error
        console.log('GLOBAL - notification modal background not found');
        return
    }

    return notificationModalBlur;
}

export function swapNotificationModalVisability() {
    try {
        var notificationModalBlur = getNotificationModalBlurElement()
    } catch(err) {
        console.error(err.message)
        return
    }

    if (notificationModalBlur.style.display == "none") {
        showNotificationModal(notificationModalBlur)
    } else {
        hideNotificationModal(notificationModalBlur)
    }
}

export function hideNotificationModal(back: HTMLDivElement) {
    back.style.display = 'none';
}

export function showNotificationModal(back: HTMLDivElement) {
    back.style.display = 'flex';
}
