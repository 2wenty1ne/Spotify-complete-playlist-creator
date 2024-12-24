import { handleErr } from "./err/err";
import { handleModal } from "./notificationModal";
import { handleHome } from "./home/home"

//TODO show error message on screen if html element not found instead of console.err
//TODO -> global error function to send error alert
document.addEventListener('DOMContentLoaded', () => {
    const bodyId = document.body.id;

    if (bodyId === "homepage") {
        handleHome()
    }

    else if (bodyId === "errorpage") {
        handleErr()
    }

    handleModal()
});

