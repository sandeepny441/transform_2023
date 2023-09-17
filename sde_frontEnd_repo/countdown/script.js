let countdown; // global timer variable

function startTimer() {
    const timerDisplay = document.getElementById('timer');
    const totalTime = 10 * 60; // 10 minutes in seconds
    let timeLeft = totalTime;

    clearInterval(countdown); // clear any existing timers

    countdown = setInterval(function () {
        // calculate minutes and seconds
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        
        // display the time
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

        if (timeLeft <= 0) {
            clearInterval(countdown);
            alert('Time is up!');
        }

        timeLeft--;
    }, 1000); // update every second
}
