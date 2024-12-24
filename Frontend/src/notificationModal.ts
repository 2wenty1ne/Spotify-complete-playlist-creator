
export function handleModal() {
    const modalCloseButton: HTMLButtonElement = document.querySelector('#close-modal-button') as HTMLButtonElement;
    if (!modalCloseButton) {
        //! Internal Server Error
        console.error('GLOBAL - notification modal close button not found')
        return
    }
    
    modalCloseButton.addEventListener('click', () => {
        try {
            var notificationModal = getNotificationModalElement()
        } catch (err) {
            return;
        }
        hideNotificationModal(notificationModal)
    });
}

export function sendNotifactionModal() {
    try {
        var modalElement = getNotificationModalElement()
    } catch (err) {
        console.error(err.message)
        return;
    }
    
} 


export function getNotificationModalElement() {
    const notificationModal: HTMLDivElement = document.querySelector('#notification-modal') as HTMLDivElement;
    if (!notificationModal) {
        //! Internal Server Error
        console.log('GLOBAL - notification modal not found');
        throw Error("GLOBAL - notification modal not found");
    }

    return notificationModal;
}

export function swapNotificationModalVisability() {
    try {
        var notificationModal = getNotificationModalElement()
    } catch(err) {
        console.error(err.message)
        return
    }

    if (notificationModal.style.display == "none") {
        showNotificationModal(notificationModal)
    } else {
        hideNotificationModal(notificationModal)
    }
}

export function hideNotificationModal(modal: HTMLDivElement) {
    modal.style.display = 'none';
}

export function showNotificationModal(modal: HTMLDivElement) {
    modal.style.display = 'flex';
}